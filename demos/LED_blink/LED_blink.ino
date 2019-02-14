#define LEDpin 1
#define readPin A0
#define LEDpinRED 10

void setup() {
  for(int i= 2; i < 6; i++){
    pinMode(i, INPUT);
  }

}

void loop() {
  for(int i= 2; i < 6; i++){
    digitalWrite(i, HIGH);
    delay(100);
    digitalWrite(i, LOW);
  }

}
