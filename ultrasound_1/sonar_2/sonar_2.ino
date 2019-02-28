#include <MPU6050_tockn.h>
#include <Wire.h>
#define trigger 13
#define echo 2

MPU6050 mpu6050(Wire);

long timer = 0;

void setup() {
  pinMode(trigger, OUTPUT);
  pinMode(echo, INPUT);
  Serial.begin(9600);
  Wire.begin();
  mpu6050.begin();
  mpu6050.calcGyroOffsets(true);
}

void loop() {
  mpu6050.update();

  if(millis() - timer > 1000){
    
    Serial.println("=======================================================");
    Serial.print("temp : ");Serial.println(mpu6050.getTemp());

    
    Serial.print("angleX : ");Serial.print(mpu6050.getAngleX());
    Serial.print("\tangleY : ");Serial.print(mpu6050.getAngleY());
    Serial.print("\tangleZ : ");Serial.println(mpu6050.getAngleZ());
    Serial.println("=======================================================\n");

    digitalWrite(trigger, HIGH);
    digitalWrite(trigger, LOW);
    float timeIn = pulseIn(echo, HIGH);
    float distance = timeIn*0.0343*0.5;
    Serial.println("\tDistance: ");Serial.println(distance);
    
    timer = millis();

    
    
  }

}
