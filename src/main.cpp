#include <WiFi.h>
#include <HTTPClient.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

#define SCREEN_WIDTH 128
#define SCREEN_HEIGHT 64

#define BUTTON_PIN 4

const char* ssid = "Wokwi-GUEST";
const char* password = "";

// CHANGE THIS
const char* serverUrl =
"http://YOUR_PC_IP:5000/open_workspace";

Adafruit_SSD1306 display(
  SCREEN_WIDTH,
  SCREEN_HEIGHT,
  &Wire,
  -1
);

void showMessage(String msg)
{
  display.clearDisplay();

  display.setTextSize(1);
  display.setCursor(0,0);

  display.println(msg);

  display.display();
}

void sendCommand()
{
  if(WiFi.status() != WL_CONNECTED)
  {
    showMessage("WiFi Error");
    return;
  }

  HTTPClient http;

  http.begin(serverUrl);

  int code = http.GET();

  if(code > 0)
  {
    showMessage("Apps Opened");
  }
  else
  {
    showMessage("Server Error");
  }

  http.end();
}

void setup()
{
  Serial.begin(115200);

  pinMode(BUTTON_PIN, INPUT_PULLUP);

  Wire.begin(8,9);

  display.begin(
    SSD1306_SWITCHCAPVCC,
    0x3C
  );

  showMessage("Connecting WiFi");

  WiFi.begin(
    ssid,
    password
  );

  while(
    WiFi.status()
    != WL_CONNECTED
  )
  {
    delay(500);
  }

  showMessage("Ready");
}

void loop()
{
  if(digitalRead(BUTTON_PIN)==LOW)
  {
    showMessage("Opening VSCode");

    sendCommand();

    delay(2000);

    showMessage("Ready");
  }
}