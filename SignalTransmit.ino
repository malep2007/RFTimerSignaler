#include <SoftwareSerial.h>
SoftwareSerial mySerial = SoftwareSerial(0,1);
int counter = 0;
void setup()
{
  String msg = "AT";
  mySerial.begin(9600);
  Serial.begin(9600);
  Serial.println("Sending message to serial port");
}

void loop()
{
  Serial.println("Start");
  delay(1000);
  
  //delay(3000);
}

