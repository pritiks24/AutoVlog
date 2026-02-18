# 🤖 Gemini AI Integration Guide

## What Changed?

Your video transformer now uses **Google's Gemini AI API** instead of simple keyword matching. This means:

✅ **Smarter Transformations** - Gemini understands your intent, not just keywords  
✅ **Natural Language** - Describe what you want in plain English  
✅ **Intelligent Effects** - AI suggests the best effect and intensity level  
✅ **More Creative** - Try poetic descriptions, Gemini will understand  

### Before vs. After

**OLD (Keyword-based):**
```
User: "Make video black and white"
App: Checks if "black" or "white" in prompt
Result: Applies grayscale
```

**NEW (Gemini AI):**
```
User: "Make it look like an old film"
Gemini: Analyzes prompt
Suggests: {"effect": "sepia", "intensity": 8}
Result: Beautiful vintage effect with optimized intensity
```

---

## How to Set Up (2 minutes)

### Step 1: Get Gemini API Key

1. Go to: **https://ai.google.dev/**
2. Click **"Get API Key"**
3. Sign in with Google
4. Click **"Create API Key"**
5. **Copy the key** (it starts with `AIza`)

### Step 2: Create `.env` File

In your project folder, create a file named `.env`:

```
GEMINI_API_KEY=paste_your_key_here
```

Or use the template:
```bash
cp .env.example .env
# Edit and add your key
```

### Step 3: Install & Run

```bash
# Install dependencies (includes Gemini client)
pip install -r requirements.txt

# Run the app
python app.py

# Visit: http://localhost:5000
```

---

## How Gemini Integration Works

### The Flow

```
┌─────────────────────────────────────────┐
│  User enters prompt in browser          │
│  "Make it look like a vintage photo"    │
└─────────────────┬───────────────────────┘
                  │
                  ▼
        ┌─────────────────────┐
        │  Send to Gemini API │
        │  (google cloud)     │
        └─────────┬───────────┘
                  │
                  ▼
    ┌─────────────────────────────────┐
    │  Gemini analyzes the prompt     │
    │ Returns transformation params:  │
    │ {                               │
    │   "effect": "sepia",           │
    │   "intensity": 8,              │
    │   "description": "Applied...",  │
    │   "parameters": {...}           │
    │ }                               │
    └─────────────┬───────────────────┘
                  │
                  ▼
    ┌──────────────────────────────────┐
    │  Flask backend processes video   │
    │  - Loads video frames            │
    │  - Applies Gemini's suggested    │
    │    effect with intensity         │
    │  - Saves processed video         │
    └──────────────┬───────────────────┘
                   │
                   ▼
         ┌─────────────────────┐
         │  Returns result     │
         │  - Video URL        │
         │  - Effect details   │
         │  - Frame count      │
         └──────────┬──────────┘
                    │
                    ▼
      ┌──────────────────────────────┐
      │  Browser displays:           │
      │  - Processed video           │
      │  - Effect type and intensity │
      │  - Download button           │
      └──────────────────────────────┘
```

### What Gemini Understands

You can use ANY description and Gemini will figure it out:

**Specific requests:**
- "Convert to grayscale"
- "Apply a blur effect"
- "Sharpen the video"

**Creative requests:**
- "Make it look like a painting"
- "Vintage film from the 80s"
- "Dreamy and soft"
- "High contrast comic book style"

**Emotional requests:**
- "Make it feel nostalgic"
- "Dramatic and dark"
- "Bright and cheerful"

**Technical requests:**
- "Increase saturation to maximum"
- "Edge detection with threshold"
- "Motion blur effect"

---

## Supported Transformations

Gemini can suggest any of these effects based on your prompt:

| Effect | When Suggested | Example Prompt |
|--------|---|---|
| **grayscale** | B&W, monochrome requests | "Make it black and white" |
| **blur** | Soft, dreamy, hazy requests | "Make it dreamy and soft" |
| **sharpen** | Detail, crisp, detail requests | "Enhance the sharpness" |
| **edge_detect** | Edge, outline, contour requests | "Show me the edges" |
| **brighten** | Bright, light, sunlit requests | "Make it brighter" |
| **darken** | Dark, moody, night requests | "Make it darker" |
| **invert** | Negative, inverse requests | "Negative effect" |
| **saturation** | Vibrant, color, vivid requests | "Make colors pop" |
| **sepia** | Vintage, old, retro requests | "Make it look old" |
| **flip** | Mirror, reverse requests | "Flip it horizontally" |
| **posterize** | Comic, poster, art requests | "Comic book style" |
| **motion_blur** | Action, speed, motion requests | "Motion blur effect" |

---

## API Quotas & Pricing

### Free Tier (What You Get)
- ✅ **60 requests per minute** - Plenty for testing
- ✅ **Unlimited per day** (within quota)
- ✅ **No credit card required**
- ✅ Perfect for development

### Pricing (If you scale)
- Gemini 1.5 Flash: $0.075 per 1M input tokens
- Gemini 1.5 Pro: $7.50 per 1M input tokens

> **For your use case:** Free tier is more than enough!

### Monitoring Your Usage

Check your API usage:
1. Go to: https://console.cloud.google.com/
2. Select your project
3. Go to **APIs & Services** → **Quotas**
4. Find **Generative Language API**
5. View your requests/minute

---

## Example Workflows

### Example 1: Vintage Photo Effect
```
User prompt: "Make it look like a photo from the 1970s"
         ↓
Gemini suggests: sepia effect (intensity: 7)
         ↓
Result: Beautiful warm, vintage-looking video
```

### Example 2: Artistic Illustration
```
User prompt: "Convert to a comic book style illustration"
         ↓
Gemini suggests: posterize effect (intensity: 6)
         ↓
Result: Reduced colors, comic-like appearance
```

### Example 3: Detail Enhancement
```
User prompt: "I want to see all the details clearly"
         ↓
Gemini suggests: sharpen effect (intensity: 8)
         ↓
Result: Enhanced edges, crisp, detailed video
```

### Example 4: Moody Atmosphere
```
User prompt: "Dark and moody, like a noir film"
         ↓
Gemini suggests: darken + invert (intensity: 6)
         ↓
Result: Dramatic, dark atmospheric video
```

---

## Environment Variables Explained

Your `.env` file contains:

```ini
# Your Gemini API key (keep this SECRET!)
GEMINI_API_KEY=AIza...your_key_here...

# Flask configuration (optional)
FLASK_ENV=development
FLASK_DEBUG=True
```

### Important ⚠️

**Never share your API key!**
- Don't commit `.env` to Git
- Don't share in Discord/Slack
- Add `.env` to `.gitignore` (already done)

---

## Troubleshooting Gemini Integration

### Problem: "GEMINI_API_KEY not found"

**Solution:**
```bash
# Make sure .env file exists in project root
ls -la | grep .env

# If missing, create it
cp .env.example .env

# Edit and add your key
# GEMINI_API_KEY=AIza...
```

### Problem: "Failed to configure Gemini API"

**Check your API key:**
1. Visit: https://ai.google.dev/
2. Go to settings
3. Verify key is valid
4. Copy exact key (no spaces)
5. Update `.env` file

### Problem: "Gemini API error"

**In console, you might see:**
```
Gemini API error: Invalid API key
```

**Solutions:**
1. Check `.env` has correct key
2. Verify API is enabled in Google Cloud
3. Check internet connection
4. Try re-authenticating the key

### Problem: API quota exceeded

**If you see:**
```
Resource has been exhausted
```

**Don't worry!** Free tier resets daily. Just wait a bit.

---

## Customizing the Integration

### Change the Model

Edit `app.py`, find this line:
```python
model = genai.GenerativeModel('gemini-1.5-flash')
```

Other available models:
- `gemini-1.5-flash` (fastest, recommended)
- `gemini-1.5-pro` (more accurate, slower)
- `gemini-pro` (standard, balanced)

### Adjust Effect Suggestions

Edit the prompt in `get_transformation_from_gemini()` function:

```python
message = f"""You are a video processing expert...
Analyze this request and return JSON with:
...
Add this to the list of effects you can suggest:
- posterize_aggressive: More extreme color reduction
...
"""
```

### Add Custom Effects

Edit `process_video_with_prompt()` and add:

```python
elif effect == "your_new_effect":
    # Your OpenCV code here
    frame = cv2.yourFunction(frame)
```

---

## API Reference

### Gemini Model: `gemini-1.5-flash`

**What it does:**
- Understands natural language prompts
- Analyzes video transformation requests
- Suggests appropriate effects and intensity
- Returns structured JSON

**Input:**
- User's text prompt (any length)
- Optional: sample frame for analysis

**Output (JSON):**
```json
{
  "effect": "string",
  "intensity": 1-10,
  "description": "string",
  "parameters": {}
}
```

**Rate Limits (Free)**
- 60 requests/minute
- 1500 requests/day

---

## Performance Tips

✅ **Gemini calls are fast** - Usually <1 second  
✅ **Video processing is slower** - Depends on video duration  
✅ **Cache results** - Use same prompt = same result  
✅ **Batch processing** - Process multiple videos efficiently

### Typical Timeline:
```
1. User submits prompt → Network to Google: ~100ms
2. Gemini analyzes prompt → AI processing: ~500ms
3. Flask processes video → Frame-by-frame: depends on duration
   - 5 seconds @ 15fps = 75 frames
   - Each frame processing: ~10-50ms
   - Total: 30-120 seconds (typical)
```

---

## Comparison: Before vs. After

### Before (Keyword Matching)
```python
if "grayscale" in prompt.lower():
    apply_grayscale()
elif "blur" in prompt.lower():
    apply_blur()
else:
    apply_default_effect()
```

❌ Limited to exact keywords  
❌ No understanding of intent  
❌ Rigid and inflexible  

### After (Gemini AI)
```python
transformation = get_transformation_from_gemini(prompt)
apply_effect(transformation['effect'], transformation['intensity'])
```

✅ Understands natural language  
✅ Grasps user intent  
✅ Flexible and creative  
✅ Intelligent intensity selection  

---

## Security & Privacy

### Your Data
- ✅ Prompts sent to Google (encrypted)
- ✅ Video frames NOT sent to Gemini
- ✅ Only text analysis happens
- ✅ Results stored locally

### Your API Key
- ⚠️ Keep it private!
- ⚠️ Don't commit to GitHub
- ⚠️ Rotate if compromised
- ✅ Use `.env` file (not in code)

---

## Next Steps

1. ✅ Get Gemini API key
2. ✅ Create `.env` file
3. ✅ Install dependencies
4. ✅ Run the app
5. ✅ Try creative prompts!

---

## Resources

| Resource | Link |
|----------|------|
| Google AI | https://ai.google.dev/ |
| API Docs | https://ai.google.dev/docs |
| Getting Started | https://ai.google.dev/tutorials/python_quickstart |
| Python Library | https://github.com/google/generative-ai-python |
| Console | https://console.cloud.google.com/ |

---

## Questions?

Refer to:
- [HOW_TO_RUN.md](HOW_TO_RUN.md) - Setup instructions
- [README.md](README.md) - Full documentation
- [QUICKSTART.md](QUICKSTART.md) - Quick reference
- `.env.example` - Environment template

---

**Enjoy AI-powered video transformations! 🚀🤖✨**
