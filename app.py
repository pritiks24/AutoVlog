import os
import time
import cv2
import json
import numpy as np
from flask import Flask, render_template, request, send_from_directory, jsonify
from werkzeug.utils import secure_filename
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

app = Flask(__name__)

UPLOADS = "uploads"
PROCESSED = "processed"
os.makedirs(UPLOADS, exist_ok=True)
os.makedirs(PROCESSED, exist_ok=True)

# Configure Gemini API
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
if GEMINI_API_KEY:
    genai.configure(api_key=GEMINI_API_KEY)

# Video processing helpers
def get_transformation_from_gemini(prompt, sample_frame_path=None):
    """
    Use Gemini API to understand the user's prompt and return transformation parameters.
    Can analyze a sample frame if provided.
    """
    try:
        model = genai.GenerativeModel('gemini-2.5-flash')
        
        message = f"""You are a video processing expert. The user wants to transform their video with this prompt:
"{prompt}"

Analyze this request and return a JSON response with:
1. "effect" - the primary effect name (e.g., "grayscale", "blur", "brighten", "edge_detect")
2. "intensity" - intensity level from 1-10 (10 being strongest)
3. "description" - brief description of what will be applied
4. "parameters" - any specific parameters as a dict

Return ONLY valid JSON, no other text.

Common effects you can suggest:
- grayscale: convert to black and white
- blur: apply gaussian blur
- sharpen: enhance edges
- edge_detect: detect edges with canny algorithm
- brighten: increase brightness
- darken: decrease brightness
- invert: invert colors
- saturation: boost color saturation
- sepia: apply sepia tone
- flip: mirror horizontally
- posterize: reduce colors to create poster effect
- motion_blur: apply motion blur effect

Example: {{"effect": "blur", "intensity": 5, "description": "Applied medium blur effect", "parameters": {{"kernel_size": 15}}}}
"""
        
        response = model.generate_content(message)
        
        try:
            result = json.loads(response.text)
            return result
        except json.JSONDecodeError:
            # Fallback to default effect if parsing fails
            return {
                "effect": "blur",
                "intensity": 3,
                "description": "Applied default blur effect",
                "parameters": {"kernel_size": 9}
            }
    except Exception as e:
        print(f"Gemini API error: {e}")
        # Return fallback effect
        return {
            "effect": "grayscale",
            "intensity": 5,
            "description": "Applied default grayscale effect",
            "parameters": {}
        }

def process_video_with_prompt(input_path, prompt, output_path):
    """
    Process video based on user prompt using Gemini API.
    Gemini analyzes the prompt and applies intelligent transformations.
    """
    # Get transformation parameters from Gemini
    transformation = get_transformation_from_gemini(prompt)
    effect = transformation.get("effect", "blur").lower()
    intensity = transformation.get("intensity", 5)
    parameters = transformation.get("parameters", {})
    
    cap = cv2.VideoCapture(input_path)
    
    fps = cap.get(cv2.CAP_PROP_FPS) or 15
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 640)
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 480)
    
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    writer = cv2.VideoWriter(output_path, fourcc, fps, (width, height))
    
    frame_count = 0
    while True:
        ok, frame = cap.read()
        if not ok:
            break
        
        # Apply transformation based on Gemini's analysis
        if effect == "grayscale":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
        
        elif effect == "blur":
            kernel_size = parameters.get("kernel_size", int(5 + intensity * 2))
            if kernel_size % 2 == 0:
                kernel_size += 1
            frame = cv2.GaussianBlur(frame, (kernel_size, kernel_size), 0)
        
        elif effect == "sharpen":
            # Create sharpening kernel
            factor = intensity / 5.0
            kernel = np.array([[-1, -1, -1],
                              [-1,  5 + (factor * 3), -1],
                              [-1, -1, -1]]) * factor
            frame = cv2.filter2D(frame, -1, kernel)
        
        elif effect == "edge_detect":
            threshold = parameters.get("threshold", int(50 + (10 - intensity) * 10))
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            edges = cv2.Canny(gray, threshold, threshold * 2)
            frame = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)
        
        elif effect == "flip":
            frame = cv2.flip(frame, 1)
        
        elif effect == "rotate":
            rows, cols = frame.shape[:2]
            rotation_matrix = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
            frame = cv2.warpAffine(frame, rotation_matrix, (cols, rows))
        
        elif effect == "brighten":
            factor = 1.0 + (intensity / 10.0)
            frame = cv2.convertScaleAbs(frame, alpha=factor, beta=intensity * 5)
        
        elif effect == "darken":
            factor = 1.0 - (intensity / 15.0)
            frame = cv2.convertScaleAbs(frame, alpha=factor, beta=-intensity * 3)
        
        elif effect == "invert":
            frame = cv2.bitwise_not(frame)
        
        elif effect == "saturation":
            hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV).astype(np.float32)
            hsv[:,:,1] = hsv[:,:,1] * (1.0 + intensity / 10.0)
            hsv[:,:,1] = np.clip(hsv[:,:,1], 0, 255)
            frame = cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)
        
        elif effect == "sepia":
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB).astype(np.float32)
            kernel = np.array([[0.272, 0.534, 0.131],
                               [0.349, 0.686, 0.168],
                               [0.393, 0.769, 0.189]])
            frame = cv2.transform(frame, kernel)
            frame = np.clip(frame, 0, 255).astype(np.uint8)
            frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
        
        elif effect == "posterize":
            # Reduce color levels
            levels = max(2, int(8 - intensity / 2))
            frame = (frame // (256 // levels)) * (256 // levels)
        
        elif effect == "motion_blur":
            # Apply motion blur
            size = int(5 + intensity * 2)
            kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (size, size))
            frame = cv2.filter2D(frame, -1, kernel)
        
        writer.write(frame)
        frame_count += 1
    
    cap.release()
    writer.release()
    
    return frame_count, transformation

@app.get("/")
def home():
    return render_template("index.html")

@app.post("/capture")
def capture():
    try:
        ip = request.form["ip"].strip()
        seconds = int(request.form.get("seconds", 5))

        candidates = [
            f"http://{ip}:81/stream",
            f"http://{ip}/stream",
            f"http://{ip}/video",
        ]

        cap = None
        for url in candidates:
            temp = cv2.VideoCapture(url)
            if temp.isOpened():
                cap = temp
                break

        if cap is None:
            return jsonify({"error": f"Could not open ESP32 stream. Tried: {candidates}"}), 400

        out_name = f"capture_{int(time.time())}.mp4"
        out_path = os.path.join(UPLOADS, out_name)

        fps = cap.get(cv2.CAP_PROP_FPS)
        if not fps or fps < 2:
            fps = 15

        width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH) or 640)
        height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT) or 480)

        fourcc = cv2.VideoWriter_fourcc(*"mp4v")
        writer = cv2.VideoWriter(out_path, fourcc, fps, (width, height))

        frames_to_capture = int(fps * seconds)
        for _ in range(frames_to_capture):
            ok, frame = cap.read()
            if not ok:
                break
            writer.write(frame)

        cap.release()
        writer.release()

        return jsonify({
            "success": True,
            "video_url": f"/uploads/{out_name}",
            "filename": out_name
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.post("/process")
def process():
    try:
        data = request.json
        video_file = data.get("video_file")
        prompt = data.get("prompt", "").strip()
        
        if not video_file or not prompt:
            return jsonify({"error": "Missing video file or prompt"}), 400
        
        input_path = os.path.join(UPLOADS, secure_filename(video_file))
        
        if not os.path.exists(input_path):
            return jsonify({"error": "Video file not found"}), 404
        
        out_name = f"processed_{int(time.time())}.mp4"
        output_path = os.path.join(PROCESSED, out_name)
        
        frame_count, transformation = process_video_with_prompt(input_path, prompt, output_path)
        
        return jsonify({
            "success": True,
            "video_url": f"/processed/{out_name}",
            "filename": out_name,
            "frames_processed": frame_count,
            "transformation": transformation
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.get("/uploads/<path:filename>")
def serve_upload(filename):
    return send_from_directory(UPLOADS, secure_filename(filename))

@app.get("/processed/<path:filename>")
def serve_processed(filename):
    return send_from_directory(PROCESSED, secure_filename(filename))

if __name__ == "__main__":
    app.run(debug=True)