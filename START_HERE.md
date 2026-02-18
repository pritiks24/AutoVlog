# 🎬 ESP32 Video Transformer with Gemini AI - START HERE

> **⏱️ Total Setup Time: 5 minutes**

---

## 🚀 Quick Start (Copy-Paste Ready)

### Step 1: Get Free Gemini API Key (2 min)
Go to: **https://ai.google.dev/** → Click **"Get API Key"** → Copy your key

### Step 2: Configure Project (1 min)
In your project folder, create `.env` file:
```
GEMINI_API_KEY=your_key_here
```

### Step 3: Install & Run (2 min)
```bash
pip install -r requirements.txt
python app.py
```

### Step 4: Open Browser
```
http://localhost:5000
```

✨ **Done! You're ready to transform videos with AI!**

---

## 📖 Full Setup Guide (If you need more details)

### What You Need
- ✅ Python 3.8+
- ✅ Google account (free)
- ✅ Internet connection
- ✅ Web browser
- ✅ This project folder

---

## 🔑 Step 1: Get Your Gemini API Key

**Super simple:**

1. Visit: https://ai.google.dev/
2. Click **"Get API Key"** button
3. Sign in with Google
4. Click **"Create API Key"** (or select existing project)
5. **Copy the key** (looks like: `AIzaSy...`)
6. ✅ Done! Now to Step 2

> **Free forever?** Yes! 60 requests/minute free tier. Perfect for testing.

---

## 🗂️ Step 2: Create `.env` File

### Option A: Using Terminal

**macOS/Linux:**
```bash
cd /Users/pritikalahiri/Downloads/robotfun
cp .env.example .env
nano .env
# Type: GEMINI_API_KEY=your_key_here
# Save: Ctrl+X → Y → Enter
```

**Windows (Command Prompt):**
```bash
cd C:\Users\YourName\Downloads\robotfun
copy .env.example .env
notepad .env
# Add: GEMINI_API_KEY=your_key_here
# Save: Ctrl+S
```

### Option B: Manual File Creation

1. Open your text editor (VS Code, Notepad, etc.)
2. Create new file
3. Paste this:
```
GEMINI_API_KEY=your_gemini_api_key_here
```
4. Save as `.env` in project folder (same location as `app.py`)

### Verify it worked:
```bash
cat .env
# Should show: GEMINI_API_KEY=AIza...
```

---

## 📦 Step 3: Install Dependencies

```bash
# Navigate to project (macOS/Linux)
cd /Users/pritikalahiri/Downloads/robotfun

# Or Windows
cd C:\Users\YourName\Downloads\robotfun

# Install all required packages
pip install -r requirements.txt
```

**This installs:**
- Flask (web server)
- OpenCV (video processing)
- NumPy (math)
- Google Generative AI (Gemini API client)
- Python-dotenv (reads .env file)

**You should see:**
```
Successfully installed flask-3.0.0
Successfully installed opencv-python-4.8.1.78
...
Successfully installed google-generativeai-0.3.1
Successfully installed python-dotenv-1.0.0
```

---

## ▶️ Step 4: Run the Application

```bash
python app.py
```

**You should see:**
```
 * Serving Flask app 'app'
 * Debug mode: on
 * Running on http://127.0.0.1:5000
 * Press CTRL+C to quit
```

### If it doesn't work:

**Port already in use?**
```bash
# Use different port
# Edit app.py, last line:
# app.run(debug=True, port=5001)

python app.py
# Visit: http://localhost:5001
```

**Module not found?**
```bash
# Reinstall dependencies
pip install -r requirements.txt --upgrade
```

**Can't find python?**
```bash
# Use python3 instead
python3 app.py
```

---

## 🌐 Step 5: Open in Browser

Go to: **http://localhost:5000**

You should see:
```
🎬 ESP32 Video Transformer
Capture video from your ESP32 and transform it with AI-powered prompts
```

✨ **That's it! Your app is running!**

---

## 🎯 How to Use

### Column 1: Capture & Transform

**Capture Section:**
1. Enter ESP32 IP (e.g., `192.168.1.45`)
2. Set duration (seconds)
3. Click **"Capture Video"**
4. See video appear in right column

**Transform Section:**
1. Type what you want: *"Make it black and white"*
2. Or click a suggestion button
3. Click **"Process Video"**
4. AI processes the video
5. Download the result!

### Column 2: Video Display

- **Top:** Original video from ESP32
- **Bottom:** Transformed video with effect details
- **Download button:** Save your video

---

## 🤖 Try These Prompts

**Creative prompts (Gemini understands these!):**

```
"Make it look like an old film"
"Vintage photograph from the 70s"
"Dark and moody like a noir movie"
"Bright and cheerful"
"Show me only the edges"
"Comic book style"
"Dreamy and soft"
"High contrast and dramatic"
```

**Specific prompts:**

```
"Convert to grayscale"
"Apply blur"
"Sharpen the details"
"Invert the colors"
"Motion blur effect"
```

Each one does something different!

---

## 📁 Project Structure

```
robotfun/
├── app.py                 ← Main app (Flask server)
├── templates/
│   └── index.html        ← Web interface
├── .env                  ← Your API key (create this!)
├── .env.example          ← Template (reference)
├── requirements.txt      ← Dependencies list
├── uploads/              ← Captured videos (created by app)
├── processed/            ← Transformed videos (created by app)
│
└── Documentation:
    ├── HOW_TO_RUN.md     ← Detailed setup guide
    ├── GEMINI_GUIDE.md   ← How Gemini AI works
    ├── README.md         ← Full documentation
    └── QUICKSTART.md     ← Quick reference
```

---

## 🔌 Using With ESP32 Camera

### Quick Setup:
1. Upload `esp32_camera.ino` to your ESP32-CAM
2. Update WiFi credentials (lines 10-11)
3. Power on ESP32
4. Note the IP address from serial monitor
5. Enter IP in web app

### Without ESP32?
You can test the app without a camera:
- Manual video upload feature (can be added)
- Use sample videos for testing
- Focus on transformation effects first

---

## ⚙️ What Gemini AI Does

**Before:**
```
You: "Make it dreamy"
Old system: Doesn't understand → Fails
```

**After:**
```
You: "Make it dreamy"
Gemini: "I'll apply a soft blur effect with intensity 7"
Result: Beautiful dreamy video! 
```

**It understands:**
- Natural language (any description)
- Creative requests
- Technical specifications
- Emotional intent

---

## 🐛 Troubleshooting

### "ModuleNotFoundError: No module named 'google'"
```bash
pip install -r requirements.txt
```

### "GEMINI_API_KEY not found"
1. Check `.env` exists in project folder
2. Check file has your API key
3. Restart `python app.py`

### "Can't connect to localhost:5000"
1. Make sure Flask is running (should see the startup message)
2. Check port 5000 isn't used (change to 5001)
3. Try: `http://localhost:5000` in browser

### "Gemini API error"
1. Check internet connection
2. Verify API key is correct
3. Check API is enabled in Google Cloud

### "Port 5000 already in use"
```bash
# Edit last 2 lines of app.py:
# app.run(debug=True, port=5001)

python app.py
# Visit: http://localhost:5001
```

---

## 💡 Pro Tips

✅ **Shorter videos process faster** (use 5-10 seconds)  
✅ **Try creative prompts** -Gemini is smart!  
✅ **Keep API key private** - Don't share it  
✅ **Free tier is enough** - Test without limits  
✅ **Check Flask console** - See what's happening  

---

## 📚 Documentation

| Document | Purpose |
|----------|---------|
| **HOW_TO_RUN.md** | Complete setup guide with troubleshooting |
| **GEMINI_GUIDE.md** | How AI integration works |
| **README.md** | Full technical documentation |
| **QUICKSTART.md** | Quick reference guide |
| **esp32_camera.ino** | Arduino code for camera |
| **.env.example** | Configuration template |

---

## 🎬 Workflow Example

```
1. Open http://localhost:5000
   ↓
2. Enter ESP32 IP: 192.168.1.45
   ↓
3. Click "Capture Video" (5 seconds)
   ↓
4. See original video appear
   ↓
5. Type prompt: "Make it look vintage"
   ↓
6. Click "Process Video"
   ↓
7. Gemini analyzes "vintage" → suggests sepia effect
   ↓
8. Flask applies sepia transformation
   ↓
9. Processed video appears with effect details
   ↓
10. Click "Download" to save
```

---

## 🚀 Next Steps

1. ✅ Create `.env` with API key
2. ✅ Run `pip install -r requirements.txt`
3. ✅ Run `python app.py`
4. ✅ Open http://localhost:5000
5. ✅ Try different prompts
6. ✅ Capture from ESP32
7. ✅ Have fun!

---

## 🆘 Still Stuck?

1. **Read HOW_TO_RUN.md** - Detailed step-by-step
2. **Check GEMINI_GUIDE.md** - AI integration details
3. **Look at Flask console** - Error messages
4. **Verify API key** - https://ai.google.dev/
5. **Check internet** - Need connection for Gemini

---

## ✨ What's New

### With Gemini AI:
✅ Natural language prompts  
✅ Intelligent effect selection  
✅ Intensity level optimization  
✅ Creative transformations  
✅ Smart parameter adjustment  

### You can now say:
- *"Make it look like a painting"*
- *"Vintage 1950s photo"*
- *"Dark and mysterious"*
- *"Bright and vibrant"*
- And Gemini understands!

---

## 📊 System Requirements

- Python 3.8+
- ~100MB disk space
- Internet (for Gemini)
- Modern browser
- Google account (free)

---

## 🎉 Ready?

```bash
cd /Users/pritikalahiri/Downloads/robotfun
python app.py
# Open: http://localhost:5000
```

**Enjoy creating amazing videos with AI! 🚀✨**

---

**Questions?** Check [HOW_TO_RUN.md](HOW_TO_RUN.md) first!
