#include <math.h>

void setup(void) {
    Serial.begin(9600);
}

double Thermister(int RawADC) {
  double Temp;
  // See http://en.wikipedia.org/wiki/Thermistor for explanation of formula
  Temp = log(((10240000/RawADC) - 10000));
  Temp = 1 / (0.001129148 + (0.000234125 * Temp) + (0.0000000876741 * Temp * Temp * Temp));
  Temp = 273.15 - Temp;           // Convert Kelvin to Celcius
  return Temp;
}

void printTemp(void)
{
  //Serial.print("Temperatura: ");
  Serial.print(Thermister(analogRead(0)));
}

void loop(void) {
  printTemp();
  delay(1000);
}



