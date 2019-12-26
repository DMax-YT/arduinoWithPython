char inChar;
#define LED_PIN 13
bool enabled = 0;

void setup() {
  pinMode(LED_PIN, OUTPUT);     // Инициализация светодиода
  Serial.begin(9600);           // Инициализация Serial - порта
}

void loop() {
  if (Serial.available() > 0){
    inChar = Serial.read();
    if (inChar == 'e') {        // e - Enable - включить
      digitalWrite(LED_PIN, HIGH);
    }
  } else if (inChar == 'd') {   // d - Disable - выключить
    digitalWrite(LED_PIN, LOW);
  } else if (inChar == 'b') {   // b - Blink - выключить режим мигания
    enabled = 1;
    do{
      inChar = Serial.read();
      digitalWrite(LED_PIN, HIGH);
      delay(1000);
      digitalWrite(LED_PIN, LOW);
      delay(1000);
      if(inChar == 'd'){
        digitalWrite(LED_PIN, LOW);
        enabled = 0;
      } else if(inChar == 'e'){
        digitalWrite(LED_PIN, HIGH);
        enabled = 0;
      }
    } while (enabled);
  }
}
