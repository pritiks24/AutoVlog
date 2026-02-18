# Quick Start Guide - ESP32 Video Transformer

## Installation (2 minutes)

### 1. Install Python Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start the Flask Server
```bash
python app.py
```

You should see:
```
 * Running on http://127.0.0.1:5000
 * Debug mode: on
```

### 3. Open in Browser
Go to: **http://localhost:5000**

---

## First Time Setup

### Step 1: Get Your ESP32 Ready
1. Upload camera code to ESP32 using Arduino IDE
2. Note down the **ESP32 IP address** (check serial monitor or router)
3. Ensure ESP32 is **streaming video** (test with: `http://<ip>:81/stream`)

### Step 2: Capture Your First Video
1. Enter ESP32 IP address in the web form
2. Set recording duration (e.g., 5 seconds)
3. Click **"Capture Video"**
4. You should see the video appear in the "Original Video" section

### Step 3: Transform the Video
1. Type a transformation prompt (e.g., "Make it grayscale")
2. Or click one of the quick suggestion buttons
3. Click **"Process Video"**
4. The transformed video appears in the "Transformed Video" section
5. Download if you want to save it

---

## Common Issues & Fixes

### Issue: "Could not open ESP32 stream"
**Solution:**
- Check IP address is correct
- Ping the ESP32: `ping 192.168.1.45`
- Ensure ESP32 is powered on and streaming
- Try accessing stream directly: `http://<esp32-ip>:81/stream`

### Issue: Video capture works but transformation doesn't
**Solution:**
- Make sure you clicked "Capture Video" first
- Ensure the "Process Video" button is enabled (not grayed out)
- Check browser console for errors (F12 → Console tab)

### Issue: Port 5000 already in use
**Solution:**
Edit `app.py` and change the port:
```python
if __name__ == "__main__":
    app.run(debug=True, port=5001)  # Use 5001 instead
```

---

## Available Transformations

### Quick Suggestions (Built-in)
- ⚫ **Grayscale** - Black and white video
- 👁️ **Blur** - Soft, blurred effect
- 🔍 **Sharpen** - Enhanced details
- ⚡ **Edge Detection** - Highlight edges
- 🔄 **Flip** - Mirror horizontally
- ☀️ **Brighten** - Increase brightness

### Custom Prompts (Try These)
| Prompt | Result |
|--------|--------|
| "darken" | Darker video |
| "invert" | Negative film effect |
| "sepia" | Vintage brown tone |
| "saturate" | More vivid colors |

---

## Tips & Tricks

✅ **Optimize Performance:**
- Use shorter video durations (1-10 seconds)
- Lower ESP32 camera resolution if possible
- Close other browser tabs

✅ **Best Results:**
- Good lighting for ESP32 camera
- Stable WiFi connection
- Clear ESP32 IP address entry

✅ **Download Videos:**
- Click the download button after processing
- Videos are saved to your Downloads folder

---

## Next Steps

1. Try different transformations
2. Experiment with custom prompts
3. Review [README.md](README.md) for advanced features
4. Check [API documentation](README.md#api-endpoints) for integration

---

## Still Having Issues?

1. Check Flask console output for error messages
2. Open browser DevTools (F12) and check the Console tab
3. Verify Flask is running: `curl http://localhost:5000`
4. Check ESP32 is streaming: Open `http://<esp32-ip>/stream` in browser

**Happy video transforming! 🎬✨**
