int InputPin = A0;
void setup() {
  // put your setup code here, to run once:
  Serial.begin( 9600 );
}

void loop() {
  // put your main code here, to run repeatedly:
    int value;
    float volt;

    value = analogRead( InputPin );

    volt = value * 5.0 / 1023.0;

    //Serial.print( "Value: " );
    Serial.println( value );
    //Serial.print( "  Volt: " );
    //Serial.println( volt );
    delay(3000);
}
