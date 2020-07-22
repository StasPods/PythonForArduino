
char inChar;

void setup() {
pinMode(2, OUTPUT);
Serial.begin(9600);
pinMode(4, OUTPUT);
}

void loop() {
 if (Serial.available() > 0)
  {
    inChar = Serial.read();
    if (inChar=='q') // e - Enable - включить
    {
      digitalWrite(2,HIGH);
      Serial.println("da1");
    }
     if (inChar=='w') // e - Enable - включить
    {
      digitalWrite(4, HIGH);
      Serial.println("da2");
    }
  
    if (inChar=='e') // d - Disable - выключить
    {
      digitalWrite(2,LOW);
      digitalWrite(4,LOW);
      Serial.println("net");
      
    }
    
  }
}
