# ESP32 Video Transformer

A web-based application that captures video streams from an ESP32 camera and applies AI-driven transformations based on user prompts.

## Features

- **Live Capture**: Connect to ESP32 camera and capture video in real-time
- **AI Transformations**: Apply various filters and effects via natural language prompts
- **Modern UI**: Beautiful, responsive web interface
- **Multiple Filters**: Grayscale, blur, sharpen, edge detection, flip, brightness, saturation, sepia, and more
- **Side-by-side Comparison**: View original and processed videos together
- **Download Support**: Download processed videos

## System Architecture

```
┌─────────────────────────────────────────┐
│          ESP32 Camera                    │
│    (Streaming video via MJPEG)          │
└──────────────┬──────────────────────────┘
               │
               │ (HTTP Stream)
               ▼
┌─────────────────────────────────────────┐
│      Flask Web Server (app.py)          │
│ - Captures video from ESP32             │
│ - Processes frames with prompts         │
│ - Serves web interface                  │
└────────────┬────────────────────────────┘
             │
    ┌────────┴────────┐
    ▼                 ▼
┌─────────────┐  ┌──────────────┐
│  uploads/   │  │  processed/  │
│(raw videos) │  │(output video)│
└─────────────┘  └──────────────┘
```

## Installation

### Prerequisites
- Python 3.8+
- Flask
- OpenCV (cv2)
- NumPy

### Setup

1. **Install dependencies:**
```bash
pip install flask opencv-python numpy
```

2. **Run the application:**
```bash
python app.py
```

3. **Access the web interface:**
Open your browser and go to: `http://localhost:5000`

## Usage

### Step 1: Capture Video from ESP32

1. Enter your **ESP32 IP address** (e.g., `192.168.1.45`)
2. Set the **recording duration** in seconds (1-60)
3. Click **"Capture Video"** button
4. The video appears in the "Original Video" section

**Finding your ESP32 IP:**
- Check your router's connected devices
- Serial monitor output from ESP32
- Use network scanning tools

### Step 2: Transform the Video

1. In the **"Transformation Prompt"** field, describe how you want to modify the video
2. Choose from **quick suggestion buttons** or write a custom prompt
3. Click **"Process Video"** button
4. Wait for processing to complete
5. View the transformed video in the **"Transformed Video"** section

### Example Prompts

| Prompt | Effect |
|--------|--------|
| "Grayscale" | Black and white video |
| "Blur" | Gaussian blur effect |
| "Sharpen" | Increase sharpness |
| "Edge detection" | Canny edge detection |
| "Flip" | Mirror horizontally |
| "Brighten" | Increase brightness |
| "Darken" | Decrease brightness |
| "Invert" | Negative filter |
| "Sepia" | Sepia tone effect |
| "Saturate" | Boost color saturation |

## Supported Transformations

### Available Filters

| Keyword | Description |
|---------|-------------|
| `grayscale`, `black and white` | Convert to grayscale |
| `blur` | Apply Gaussian blur |
| `sharpen` | Enhance edges |
| `edge`, `edges` | Edge detection (Canny) |
| `flip`, `mirror` | Mirror horizontally |
| `rotate` | Rotate 90 degrees |
| `bright`, `brighten` | Increase brightness |
| `dark`, `darken` | Decrease brightness |
| `sepia` | Sepia tone filter |
| `hue`, `saturation` | Boost color saturation |
| `invert`, `negative` | Invert colors |

## Project Structure

```
robotfun/
├── app.py                 # Flask backend with video processing
├── templates/
│   └── index.html        # Web interface (modern UI)
├── uploads/              # Captured videos from ESP32
├── processed/            # Processed/transformed videos
└── README.md             # This file
```

## API Endpoints

### `GET /`
Returns the main web interface.

**Response:** HTML page

---

### `POST /capture`
Captures video from ESP32 camera.

**Request:**
```json
{
  "ip": "192.168.1.45",
  "seconds": 5
}
```

**Response:**
```json
{
  "success": true,
  "video_url": "/uploads/capture_1612345678.mp4",
  "filename": "capture_1612345678.mp4"
}
```

---

### `POST /process`
Processes video with a prompt-based transformation.

**Request:**
```json
{
  "video_file": "capture_1612345678.mp4",
  "prompt": "Make the video grayscale"
}
```

**Response:**
```json
{
  "success": true,
  "video_url": "/processed/processed_1612345678.mp4",
  "filename": "processed_1612345678.mp4",
  "frames_processed": 75
}
```

---

### `GET /uploads/<filename>`
Serves captured video files.

---

### `GET /processed/<filename>`
Serves processed video files.

## ESP32 Setup

### Basic Example (Arduino)

```cpp
#include <WiFi.h>
#include "esp_camera.h"

const char* SSID = "YOUR_SSID";
const char* PASSWORD = "YOUR_PASSWORD";

void setup() {
  WiFi.begin(SSID, PASSWORD);
  while (WiFi.status() != WL_CONNECTED) delay(500);
  
  configInitCamera();
  startStreamServer();
}

void loop() {
  delay(10000);
}
```

For detailed ESP32 camera setup, see: [ESP32 Camera Documentation](https://docs.espressif.com/projects/esp-idf/en/latest/esp32/api-reference/peripherals/camera.html)

## Troubleshooting

### "Could not open ESP32 stream"
- Check ESP32 IP address is correct
- Ensure ESP32 is on the same network
- Verify camera is properly initialized on ESP32
- Check firewall settings

### Video doesn't show
- Ensure video format is MP4 and codec is mp4v
- Check file permissions in uploads/ and processed/ directories
- Clear browser cache and reload

### Slow processing
- Reduce video duration to speed up processing
- Close other applications to free up CPU
- Process optimization for large resolutions may be needed

### Quality loss
- Original quality is maintained during capture
- Some loss occurs during MJPEG streaming
- Ensure good ESP32 camera resolution

## Performance Tips

1. **Lower Resolution**: Use lower ESP32 camera resolution for faster processing
2. **Shorter Duration**: Capture shorter videos for quicker processing
3. **Simple Filters**: Grayscale and flip are fastest; edge detection is slower
4. **Hardware**: Run on a faster machine for real-time processing on high-res videos

## Future Enhancements

- [ ] GPU acceleration with CUDA
- [ ] ML-based object detection
- [ ] Custom filter creation
- [ ] Batch processing
- [ ] Real-time stream processing
- [ ] Advanced effects (style transfer, super-resolution)
- [ ] Cloud integration
- [ ] Multiple ESP32 support

## License

MIT License - Feel free to use and modify for your projects!

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review ESP32 documentation
3. Verify network connectivity
4. Check Flask debug output for error messages

---

**Enjoy creating amazing video transformations! 🎬✨**
