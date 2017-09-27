const int led_13 = 13;

int incomingByte = 0;
//int tON = 1000;
//int tOFF = 1000;
byte RXBuf[64];

void setup() {
  pinMode(led_13, OUTPUT);      // initialize digital pin 13 as an output.
  Serial.begin(9600);       // opens serial port, sets data rate to 9600 bps
}

void loop() {
  //blink_led(tON,tOFF);
  if (Serial.available()) {
    int nBytes = Serial.readBytes(RXBuf,sizeof(RXBuf));
    if (nBytes==2) {
      //tON  = int(RXBuf[0])*100;
      //tOFF = int(RXBuf[1])*100;
      digitalWrite(led_13, HIGH);
    //  Serial.print("tON = ");
      //Serial.print(tON, DEC);
      //Serial.print(" ms, tOFF = ");
      //Serial.print(tOFF, DEC);ccccccc
      //Serial.println(" ms");
    }
    if (nBytes==1) {
      //tON  = int(RXBuf[0])*100;
      //tOFF = int(RXBuf[1])*100;
      digitalWrite(led_13, LOW);
      //Serial.print("Confirm tON = ");
      //Serial.print(tON, DEC);
      //Serial.print(" ms, tOFF = ");
      //Serial.print(tOFF, DEC);
      //Serial.println(" ms");
    }
  }
}
