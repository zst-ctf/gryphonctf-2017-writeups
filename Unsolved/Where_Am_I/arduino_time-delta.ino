unsigned long startTime;

void setup() {
    Serial.begin(9600);

    pinMode(13, OUTPUT);
    pinMode(2, INPUT_PULLUP);

    Serial.println ("Waiting..");
}

unsigned long elapsed;
char c = 'A';
void loop() {
    if (digitalRead(2) == HIGH) {
        Serial.print("X=");
        digitalWrite(13, HIGH);
        startTime = millis(); // reset timer
        while (digitalRead(2) == HIGH);
        digitalWrite(13, LOW);
        elapsed = millis() - startTime;
        Serial.print("A=");
        Serial.println(elapsed);
    }
}

