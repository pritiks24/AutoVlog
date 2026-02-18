# 🚀 How to Run ESP32 Video Transformer with Gemini AI

## Quick Start (5 minutes)

### Step 1️⃣: Get Your Gemini API Key (2 minutes)

1. Go to **https://ai.google.dev/**
2. Click **"Get API Key"** button (top right)
3. Sign in with your Google account
4. Click **"Create API Key"** or select existing project
5. **Copy your API key** (looks like: `AIza...`)
6. Keep it safe!

> **Note:** Free tier includes 60 requests/minute. Perfect for testing!

### Step 2️⃣: Set Up Your Environment (1 minute)

1. Open terminal in project folder
2. Create `.env` file from template:
```bash
cp .env.example .env
```

3. Edit `.env` and paste your API key:
```
GEMINI_API_KEY=your_key_here
```

4. Save the file

### Step 3️⃣: Install & Run (2 minutes)

```bash
# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### Step 4️⃣: Open in Browser

Go to: **http://localhost:5000**

🎉 **You're done!**

---

## Detailed Setup Instructions

### 🔑 Getting Gemini API Key (Step-by-Step with Screenshots)

**Option 1: First-time users (Recommended)**

1. Visit: https://ai.google.dev/
2. Click **"Get Started"** or **"Get API Key"**
3. Accept terms if prompted
4. Choose a Google Cloud project:
   - **"Create new project"** for fresh setup
   - Or select existing project
5. Click **"Create API Key in existing project"**
6. ✅ Your API key appears! Copy it immediately
7. Keep the key private (don't commit to Git!)

**Option 2: Existing Google Cloud project**

1. Go to: https://console.cloud.google.com/
2. Select your project (top left)
3. Navigate to **APIs & Services** → **Credentials**
4. Click **"+ Create Credentials"** → **API Key**
5. Copy the key
6. (Optional) Restrict API key to **Generative Language API**

### 🗂️ Project Setup on Your Computer

**macOS/Linux:**
```bash
# Navigate to project
cd /Users/pritikalahiri/Downloads/robotfun

# Create virtual environment (optional but recommended)
python3 -m venv venv
source venv/bin/activate

# Copy environment template
cp .env.example .env

# Edit .env with your favorite editor
nano .env
# OR
code .env
```

**Windows:**
```bash
cd C:\Users\YourName\Downloads\robotfun

# Create virtual environment (optional)
python -m venv venv
venv\Scripts\activate

# Copy environment file
copy .env.example .env

# Edit .env
notepad .env
```

### 📦 Install Dependencies

```bash
pip install -r requirements.txt
```

This installs:
- `flask` - Web server
- `opencv-python` - Video processing
- `numpy` - Numerical computing
- `google-generativeai` - Gemini API client
- `python-dotenv` - Environment variable loading

### ▶️ Running the Application

**Simple (All platforms):**
```bash
python app.py
```

**With verbose output:**
```bash
python app.py --debug
```

**On a different port (if 5000 is busy):**
```bash
# Edit app.py, last line:
# Change: app.run(debug=True)
# To: app.run(debug=True, port=5001)

python app.py
# Then visit: http://localhost:5001
```

### 🌐 Access the Web Interface

Open your browser and go to:
```
http://localhost:5000
```

You should see the beautiful purple-gradient interface!

---

## How Gemini API Integration Works

### What Happens Behind the Scenes:

```
User enters prompt:
"Make the video dreamy and soft"
        │
        ▼
Sent to Gemini API
        │
        ▼
Gemini analyzes prompt and returns:
{
  "effect": "blur",
  "intensity": 7,
  "description": "Applied soft dreamy blur effect",
  "parameters": {"kernel_size": 21}
}
        │
        ▼
Flask applies the transformation
        │
        ▼
Video processes frame-by-frame
        │
        ▼
Result saved and displayed
```

### Supported Gemini Transformations:

The API can suggest these effects based on your prompt:
- **grayscale** - "Make it black and white"
- **blur** - "Make it dreamy"
- **sharpen** - "Enhance the details"
- **edge_detect** - "Show me the edges"
- **brighten** - "Make it brighter"
- **darken** - "Make it darker"
- **invert** - "Negative effect"
- **saturation** - "Make colors pop"
- **sepia** - "Vintage look"
- **flip** - "Mirror it"
- **posterize** - "Comic book style"
- **motion_blur** - "Add motion"

---

## Troubleshooting

### ❌ "ModuleNotFoundError: No module named 'google'"

**Solution:**
```bash
pip install google-generativeai python-dotenv
```

Or reinstall all:
```bash
pip install -r requirements.txt
```

### ❌ "GEMINI_API_KEY not found"

**Check:**
1. Do you have `.env` file in project root? (Not `.env.example`)
2. Is it in the same folder as `app.py`?
3. Does it have `GEMINI_API_KEY=your_key_here`?

**Fix:**
```bash
# Verify .env exists
ls -la | grep .env

# If missing, create it
cp .env.example .env

# Edit and add your key
nano .env
```

### ❌ "Address already in use"

Port 5000 is busy. Change the port:

**Edit `app.py`, last 2 lines:**
```python
if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Changed from 5000
```

Then run: `python app.py`  
Visit: `http://localhost:5001`

### ❌ "Failed to connect to ESP32"

1. Check ESP32 IP address is correct
2. Verify ESP32 is powered on
3. Ensure same WiFi network
4. Test manually: `http://192.168.1.45:81/stream`

### ❌ Gemini API errors appear in console

**Common causes:**
- Invalid API key - Check `.env` file
- API disabled - Enable in Google Cloud Console
- Rate limited - Wait a moment, try again
- No internet - Check connection

**Solution:**
```bash
# Test API key
python -c "
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')
response = model.generate_content('Say hello')
print(response.text)
"
```

---

## Usage Examples

### Example 1: Simple Grayscale

1. Capture video from ESP32
2. Type prompt: **"Convert to black and white"**
3. Gemini suggests: `grayscale` effect
4. Click Process
5. Done!

### Example 2: Artistic Effect

1. Capture video
2. Type prompt: **"Make it look like a vintage photograph"**
3. Gemini suggests: `sepia` effect with intensity 8
4. Click Process
5. Get vintage-looking video

### Example 3: Detail Enhancement

1. Capture video
2. Type prompt: **"Enhance all the details and make it crisp"**
3. Gemini suggests: `sharpen` effect with intensity 8
4. Process and download

---

## System Requirements Checklist

- ✅ Python 3.8 or higher
- ✅ Internet connection (for Gemini API)
- ✅ ~100MB disk space
- ✅ Google account (free)
- ✅ Modern web browser
- ✅ ESP32 camera (for video capture) - OR test without it first!

---

## Testing Without ESP32

**You can test the app without an actual ESP32!**

### Option 1: Use a local video file
Edit `templates/index.html` to add file upload option (developers can do this)

### Option 2: Create a test video
```python
import cv2
import numpy as np

# Create simple test video
out = cv2.VideoWriter('test_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), 15, (640, 480))

for i in range(75):  # 5 seconds at 15 fps
    frame = np.full((480, 640, 3), i, dtype=np.uint8)
    out.write(frame)

out.release()
print("Test video created: test_video.mp4")
```

Then manually move to `uploads/` folder to test processing.

---

## Next Steps

1. ✅ Run the app: `python app.py`
2. ✅ Try different prompts
3. ✅ Capture videos from ESP32
4. ✅ Download transformed videos
5. ✅ Explore Gemini's creativity!

---

## Tips & Best Practices

✅ **Use natural language** - Gemini understands:
- "Make it look dreamy"
- "Show me the edges"
- "Bright and vibrant"
- "Old film style"

✅ **Experiment** - Try various prompts to see what works

✅ **Performance** - Shorter videos process faster

✅ **API Quota** - Free tier: 60 requests/minute (enough for testing)

✅ **Security** - Never share your API key!

---

## Getting Help

| Issue | Solution |
|-------|----------|
| Still confused? | Read [README.md](README.md) or [QUICKSTART.md](QUICKSTART.md) |
| API issues? | Check https://ai.google.dev/docs |
| Technical problems? | Check Flask console for error messages |
| ESP32 questions? | See [esp32_camera.ino](esp32_camera.ino) |

---

## Quick Reference Commands

```bash
# Start app
python app.py

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

# Test Gemini connection
python -c "import google.generativeai as genai; print('OK')"

# View latest logs
tail -f app.log (if logging enabled)

# Kill the app
# Press: Ctrl+C
```

---

**You're all set! Start transforming videos with AI! 🚀✨**
