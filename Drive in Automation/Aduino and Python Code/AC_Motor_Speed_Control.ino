#define TRIAC 6
#define ZVC 3
int speed_val = 0;

void setup()
{
   pinMode(A0, INPUT);
   pinMode(TRIAC, OUTPUT);
   pinMode(ZVC, INPUT_PULLUP);
   attachInterrupt(digitalPinToInterrupt(ZVC),zero_crossing,FALLING)
}

void zero_crossing() 
{ 
int chop_time = (200 * speed_val); 
    delayMicroseconds(chop_time); 
    digitalWrite(TRIAC, HIGH); 
    delayMicroseconds(10); 
    digitalWrite(TRIAC, LOW); 
}

void loop() 
{ 
int pot = analogRead(A0); 
int data1 = map(pot, 0, 1023, 1, 45); 
speed_val = data1; 
}