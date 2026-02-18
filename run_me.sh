#!/bin/bash
# 🚀 ESP32 Video Transformer with Gemini - QUICK RUN SCRIPT
# Copy all commands below and paste into terminal

# Step 1: Navigate to project
cd /Users/pritikalahiri/Downloads/robotfun

# Step 2: Create .env file (if not already created)
cp -n .env.example .env
echo "✓ Created .env file"
echo ""
echo "⚠️  IMPORTANT: Edit .env and add your Gemini API key:"
echo "   Go to: https://ai.google.dev/"
echo "   Get your API key and add to .env:"
echo "   GEMINI_API_KEY=your_key_here"
echo ""

# Step 3: Install dependencies (first time only)
pip install -r requirements.txt

echo ""
echo "✓ Dependencies installed!"
echo ""
echo "🚀 Ready to run the app:"
echo ""
echo "   python app.py"
echo ""
echo "Then open: http://localhost:5000"
echo ""
