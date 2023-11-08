// joystic game development

// const int VRX_PIN = 0;
// const int VRY_PIN = 1;
const int SW_PIN = 2;

void setup()
{
    Serial.begin(19200);
    pinMode(A0, INPUT);
    pinMode(A1, INPUT);
    pinMode(2, INPUT);
}

void loop()
{
    // put your main code here, to run repeatedly:
    int xValue = analogRead(A0);
    int yValue = analogRead(A1);

    // print the values with to plot or view
    Serial.print(xValue);
    Serial.print("\t");
    Serial.println(yValue);
}
