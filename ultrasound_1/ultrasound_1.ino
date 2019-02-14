#define trigger 13
#define echo 2
void setup() {
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(trigger, HIGH);
  digitalWrite(trigger, LOW);
  float timeIn = pulseIn(echo, HIGH);
  float distance = timeIn*0.0343*0.5;
  Serial.println(distance);
  delay(10);
  

}
