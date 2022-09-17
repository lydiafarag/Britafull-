/* Britafull pressure sensor */

#define fsrpin A0
int fsrreading;

void setup() {
  Serial.begin(9600);
}
void loop() {
  // read FSR pin
  fsrreading = analogRead(fsrpin);
  Serial.println(fsrreading);
  delay(500);
}