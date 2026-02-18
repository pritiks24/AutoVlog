# Configuration Template for ESP32 Video Transformer
# Copy this file to config.py and customize it

# ========== Flask Configuration ==========
FLASK_DEBUG = True
FLASK_PORT = 5000
FLASK_HOST = "127.0.0.1"

# ========== Video Settings ==========
# Maximum seconds of video to capture
MAX_RECORD_DURATION = 60

# Target frame rate for output videos
DEFAULT_FPS = 15

# Default resolution for video output
DEFAULT_WIDTH = 640
DEFAULT_HEIGHT = 480

# Video codec
VIDEO_CODEC = "mp4v"

# ========== Video Processing ==========
# Supported transformation keywords
TRANSFORMATIONS = {
    "grayscale": "Convert to black and white",
    "blur": "Apply Gaussian blur",
    "sharpen": "Enhance edges",
    "edge": "Detect edges (Canny algorithm)",
    "flip": "Mirror horizontally",
    "rotate": "Rotate 90 degrees",
    "bright": "Increase brightness",
    "dark": "Decrease brightness",
    "sepia": "Apply sepia tone",
    "hue": "Boost color saturation",
    "invert": "Invert colors (negative)"
}

# ========== ESP32 Camera ==========
# Default ESP32 streams to try (in order)
ESP32_STREAM_URLS = [
    "http://{ip}:81/stream",
    "http://{ip}/stream",
    "http://{ip}/video"
]

# Common ESP32-CAM IP addresses for quick testing
COMMON_ESP32_IPS = [
    "192.168.1.100",
    "192.168.0.100",
    "192.168.1.45"
]

# ========== File Management ==========
# Upload directory for captured videos
UPLOAD_DIR = "uploads"

# Directory for processed videos
PROCESSED_DIR = "processed"

# Maximum file size in MB (0 = unlimited)
MAX_FILE_SIZE_MB = 500

# Auto-cleanup old files (days)
CLEANUP_AFTER_DAYS = 7

# ========== Quality Settings ==========
# Blur kernel size (must be odd)
BLUR_KERNEL_SIZE = 15

# Edge detection thresholds (Canny)
EDGE_THRESHOLD_LOW = 100
EDGE_THRESHOLD_HIGH = 200

# Brightness adjustment factors
BRIGHTEN_FACTOR = 1.5
BRIGHTEN_OFFSET = 30
DARKEN_FACTOR = 0.7
DARKEN_OFFSET = -20

# Saturation boost factor
SATURATION_BOOST = 1.5

# ========== Advanced Features ==========
# Enable GPU acceleration (if available)
USE_GPU = False

# Enable logging
ENABLE_LOGGING = True
LOG_FILE = "app.log"

# Request timeout (seconds)
REQUEST_TIMEOUT = 300

# ========== CORS Settings ==========
# Allowed origins for CORS
CORS_ORIGINS = ["*"]

# ========== Security ==========
# Secure file upload validation
SECURE_FILENAMES = True

# Allowed video formats
ALLOWED_FORMATS = [".mp4", ".avi", ".mov", ".mkv"]

# ========== Performance ==========
# Number of threads for video processing
NUM_THREADS = 4

# Enable frame caching for faster processing
CACHE_FRAMES = False

# ========== Development ==========
# Debug mode
DEBUG_MODE = True

# Verbose output
VERBOSE = True

# ========== Customization ==========
# Website title
WEBSITE_TITLE = "ESP32 Video Transformer"

# Custom CSS file (optional)
CUSTOM_CSS = None

# Dark mode (True/False)
DARK_MODE = False
