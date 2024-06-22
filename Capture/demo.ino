int analogInputPin = A0;
/** 初期設定の関数 一度だけ実行される */
void setup() {
  Serial.begin(9600);
}
/** 定期的に実行される関数 頻度はdelay関数で調整 */
void loop(){
  int val = analogRead(analogInputPin);
  Serial.println(val); // PCに結果を送信
  delay(1000);
}