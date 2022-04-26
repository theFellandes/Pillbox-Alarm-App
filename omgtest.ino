#include "ESP8266WiFi.h"
#include <Stepper.h>


const char* ssid = "wifi_name";
const char* password = "password";
#define motorPin0 5 // IN1 pin on the ULN2003A driver to pin D1 on NodeMCU board
#define motorPin1 4 // IN2 pin on the ULN2003A driver to pin D2 on NodeMCU board
#define motorPin2 0 // IN3 pin on the ULN2003A driver to pin D3 on NodeMCU board
#define motorPin3 2 // IN4 pin on the ULN2003A driver to pin D4 on NodeMCU board
float numOfSteps = 1.8; //100 steps = 180 degrees
Stepper stepper(200, motorPin0, motorPin2, motorPin1, motorPin3);
WiFiServer wifiServer(9090);
 
void setup() {
 
  Serial.begin(115200);
 
  delay(1000);
 
  WiFi.begin(ssid, password);
 
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.println("Connecting..");
  }
 
  Serial.print("Connected to WiFi. IP:");
  Serial.println(WiFi.localIP());
 
  wifiServer.begin();

  pinMode(motorPin0, OUTPUT);  
  pinMode(motorPin1, OUTPUT);  
  pinMode(motorPin2, OUTPUT);  
  pinMode(motorPin3, OUTPUT);
  stepper.setSpeed(100);
}

void loop() {
 
  WiFiClient client = wifiServer.available();
 
  if (client) {

    for(int i = 0; i < 25; i++){ //Added to test 45 degree movement
      stepper.step(10);
      delayMicroseconds(1000);
    }
    client.stop();
    Serial.println("Client disconnected");
 
  }
}
