/*
 * ESP32 Camera Stream Server
 * 
 * This sketch sets up an ESP32 with a camera to stream video over HTTP.
 * Compatible with: ESP32-CAM, OV2640 camera module
 * 
 * Setup:
 * 1. Install ESP32 board package in Arduino IDE
 * 2. Add this library: ESP32 by Espressif Systems
 * 3. Select: Tools > Board > ESP32 > AI Thinker ESP32-CAM
 * 4. Update WiFi credentials below
 * 5. Upload sketch
 */

#include "esp_camera.h"
#include <WiFi.h>
#include <WebServer.h>

// ========== WiFi Credentials ==========
const char* SSID = "YOUR_WIFI_SSID";
const char* PASSWORD = "YOUR_WIFI_PASSWORD";

// ========== Camera Pin Configuration (AI Thinker ESP32-CAM) ==========
#define PWDN_GPIO_NUM     32
#define RESET_GPIO_NUM    -1
#define XCLK_GPIO_NUM      0
#define SIOD_GPIO_NUM     26
#define SIOC_GPIO_NUM     27
#define Y9_GPIO_NUM       35
#define Y8_GPIO_NUM       34
#define Y7_GPIO_NUM       39
#define Y6_GPIO_NUM       36
#define Y5_GPIO_NUM       21
#define Y4_GPIO_NUM       19
#define Y3_GPIO_NUM       18
#define Y2_GPIO_NUM        5
#define VSYNC_GPIO_NUM    25
#define HREF_GPIO_NUM     23
#define PCLK_GPIO_NUM     22

WebServer server(80);
WebServer server_2(81);

// MJPEG stream handler
void handle_jpg_stream(void) {
  WiFiClient client = server.client();
  String response = "HTTP/1.1 200 OK\r\n";
  response += "Content-Type: multipart/x-mixed-replace; boundary=frame\r\n";
  response += "Connection: keep-alive\r\n";
  response += "\r\n";
  server.sendContent(response);

  while (client.connected()) {
    camera_fb_t * fb = esp_camera_fb_get();
    if (!fb) {
      Serial.println("Camera capture failed");
      break;
    }
    
    server.sendContent("--frame\r\n");
    server.sendContent("Content-Type: image/jpeg\r\n");
    server.sendContent("Content-Length: ");
    server.sendContent(String(fb->len));
    server.sendContent("\r\n");
    server.sendContent("\r\n");
    server.client().write(fb->buf, fb->buf_len);
    server.sendContent("\r\n");
    
    esp_camera_fb_return(fb);
    
    if (!client.connected()) break;
  }
}

// Single JPEG handler
void handle_jpg(void) {
  camera_fb_t * fb = esp_camera_fb_get();
  if (!fb) {
    server.send(500, "text/plain", "Camera capture failed");
    return;
  }
  
  server.sendHeader("Content-Type", "image/jpeg");
  server.sendHeader("Content-Length", String(fb->len));
  server.send_P(200, "image/jpeg", fb->buf, fb->buf_len);
  esp_camera_fb_return(fb);
}

// Status page
void handle_status(void) {
  String html = R"rawliteral(
    <html>
    <head>
      <meta charset="utf-8">
      <title>ESP32 Camera</title>
      <style>
        body { font-family: Arial; text-align: center; margin-top: 50px; }
        .status { padding: 20px; background: #f0f0f0; border-radius: 8px; }
        h1 { color: #667eea; }
        .endpoint { background: white; padding: 10px; margin: 10px 0; border-radius: 4px; font-family: monospace; }
      </style>
    </head>
    <body>
      <h1>📹 ESP32 Camera Stream</h1>
      <div class="status">
        <h2>Stream Endpoints</h2>
        <p class="endpoint">http://)rawliteral";
  
  html += WiFi.localIP().toString();
  html += R"rawliteral(:81/stream</p>
        <p class="endpoint">http://)rawliteral";
  
  html += WiFi.localIP().toString();
  html += R"rawliteral(:80/jpg</p>
        <p><strong>Status:</strong> ✓ Camera is streaming</p>
        <p style="color: #666; font-size: 12px;">
          Use these URLs with the Video Transformer application
        </p>
      </div>
    </body>
    </html>
  )rawliteral";
  
  server.send(200, "text/html", html);
}

void setup() {
  Serial.begin(115200);
  Serial.println("\n\n");
  Serial.println("ESP32 Camera Stream Server");
  Serial.println("==========================\n");
  
  // Configure camera
  camera_config_t config;
  config.ledc_channel = LEDC_CHANNEL_0;
  config.ledc_timer = LEDC_TIMER_0;
  config.pin_d0 = Y2_GPIO_NUM;
  config.pin_d1 = Y3_GPIO_NUM;
  config.pin_d2 = Y4_GPIO_NUM;
  config.pin_d3 = Y5_GPIO_NUM;
  config.pin_d4 = Y6_GPIO_NUM;
  config.pin_d5 = Y7_GPIO_NUM;
  config.pin_d6 = Y8_GPIO_NUM;
  config.pin_d7 = Y9_GPIO_NUM;
  config.pin_xclk = XCLK_GPIO_NUM;
  config.pin_pclk = PCLK_GPIO_NUM;
  config.pin_vsync = VSYNC_GPIO_NUM;
  config.pin_href = HREF_GPIO_NUM;
  config.pin_sda = SIOD_GPIO_NUM;
  config.pin_scl = SIOC_GPIO_NUM;
  config.pin_pwdn = PWDN_GPIO_NUM;
  config.pin_reset = RESET_GPIO_NUM;
  config.xclk_freq_hz = 20000000;
  config.pixel_format = PIXELFORMAT_JPEG;
  
  // Adjust frame size and quality
  config.frame_size = FRAMESIZE_VGA;      // 640x480
  config.jpeg_quality = 10;                // 0-63. Lower = better quality
  config.fb_count = 2;

  // Initialize camera
  esp_err_t err = esp_camera_init(&config);
  if (err != ESP_OK) {
    Serial.printf("Camera init failed with error 0x%x", err);
    return;
  }

  // Camera quality adjustments
  sensor_t * s = esp_camera_sensor_get();
  s->set_brightness(s, 0);     // brightness (-2 to 2)
  s->set_contrast(s, 0);       // contrast (-2 to 2)
  s->set_saturation(s, 0);     // saturation (-2 to 2)
  s->set_special_effect(s, 0); // no special effect
  s->set_whitebal(s, 1);       // enable white balance
  s->set_awb_gain(s, 1);       // enable auto white balance
  s->set_wb_mode(s, 0);        // auto white balance mode
  s->set_expose_ctrl(s, 1);    // enable exposure control
  s->set_aec_mode(s, 0);       // auto exposure mode
  s->set_aec_value(s, 300);    // set aec value
  s->set_gain_ctrl(s, 1);      // enable gain control
  s->set_agc_gain(s, 0);       // auto gain
  s->set_gainceiling(s, (gainceiling_t)0);
  s->set_bpc(s, 1);            // enable black pixel cancellation
  s->set_wpc(s, 1);            // enable white pixel compensation
  s->set_raw_gma(s, 1);        // enable raw gma
  s->set_lenc(s, 1);           // enable lens correction
  s->set_hmirror(s, 0);        // disable horizontal flip
  s->set_vflip(s, 0);          // disable vertical flip

  // WiFi Connection
  Serial.print("Connecting to WiFi: ");
  Serial.println(SSID);
  WiFi.mode(WIFI_STA);
  WiFi.begin(SSID, PASSWORD);

  int attempts = 0;
  while (WiFi.status() != WL_CONNECTED && attempts < 20) {
    delay(500);
    Serial.print(".");
    attempts++;
  }

  if (WiFi.status() != WL_CONNECTED) {
    Serial.println("\nFailed to connect to WiFi!");
    Serial.println("Please check SSID and password");
    return;
  }

  Serial.println("\nWiFi Connected!");
  Serial.print("IP Address: ");
  Serial.println(WiFi.localIP());
  Serial.print("Camera Stream: http://");
  Serial.print(WiFi.localIP());
  Serial.println(":81/stream");

  // Setup routes
  server.on("/", handle_status);
  server.on("/jpg", handle_jpg);
  
  server_2.on("/stream", handle_jpg_stream);

  // Start servers
  server.begin();
  server_2.begin();

  Serial.println("\nServers started!");
  Serial.println("Ready for streaming...");
  Serial.println("\nUsage with Video Transformer:");
  Serial.print("1. Enter this IP in the web app: ");
  Serial.println(WiFi.localIP());
  Serial.println("2. Set recording duration");
  Serial.println("3. Click 'Capture Video'");
  Serial.println("4. Apply transformations");
}

void loop() {
  server.handleClient();
  server_2.handleClient();
  delay(1);
}
