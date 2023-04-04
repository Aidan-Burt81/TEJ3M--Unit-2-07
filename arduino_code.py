/*

Created by: Aidan Burt

*/

#include <Servo.h>

int pos = 0;
Servo servo_9;
const int TRIG_Pin = 3;  //Initialize I/O pins
const int ECHO_Pin = 2;
long duration;  //Since PulseIn return an unsigned Long 
int distance;  //To save the distance

void setup()
{
servo_9.attach(9);
  Serial.begin(9600);   //Initialize Serial communication
}

void loop(){

delayMicroseconds(2);
  delayMicroseconds(10);  //Make Trigger pin High for 10 uS to start sending the pulse
distance = duration*0.034/2; 
    Serial.print("Distance: ");
    Serial.println(distance);

if (distance<50)
{
Serial.println("Rotate Forwards");
    // sweep the servo from 0 to 180 degrees in steps
  // of 1 degrees
for (pos = 0; pos <= 90; pos += 1) {
    // tell servo to go to position in variable 'pos'
    servo_9.write(pos);
    // wait 15 ms for servo to reach the position
    delay(15); // Wait for 15 millisecond(s)
}
    Serial.println("Rotate Backwards"); 
for (pos = 90; pos >= 0; pos -= 1) {
    // tell servo to go to position in variable 'pos'
    servo_9.write(pos);
    // wait 15 ms for servo to reach the position
    delay(15); // Wait for 15 millisecond(s)
}
} else {
Serial.print("distance: ");
for (pos = 0; pos <= 0; pos += 1) {
    // tell servo to go to position in variable 'pos'
    servo_9.write(pos);
    // wait 15 ms for servo to reach the position
    delay(15); // Wait for 15 millisecond(s)
}
}
}
