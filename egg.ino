#include <DHT.h>
#include <LiquidCrystal_I2C.h>
#include <LiquidCrystal.h>


#define DHTPIN 4
#define Type DHT11
#define relay1 5

int sensePin = 4;
DHT HT(sensePin,Type);
float ttemp;
float htemp;
float h;
float t;

//const int bulb = 5;
float T_threshold_high = 37.5;
float T_threshold_low = 36.5;

LiquidCrystal lcd(12,11,10,9,8,7);

void setup()
{
  Serial.begin(9600);
  HT.begin();
  lcd.begin(16,2); 
  //pinMode(vap,LOW);
  pinMode(relay1,OUTPUT);
  digitalWrite(relay1 , LOW);
//  digitalWrite(vap, LOW);
  lcd.setCursor(0, 0);
  //lcd.print("Temperature &");
  lcd.print(t);
  
}
void loop()
{
    t = HT.readTemperature();
    delay(500);
    Serial.print(t-1);
    lcd.setCursor(0, 0);
    lcd.print("Temperature &");
    lcd.print(t-1);
   
    if (t >= T_threshold_high)
    {
      delay(100);
      if (t >= T_threshold_high)
      {
        digitalWrite(relay1, LOW);  
       // digitalWrite(vap, LOW); //i move fan here to 
        Serial.println("Light off");
        Serial.println("fan low");
      }
    }

    if (t < T_threshold_low)
    {
      delay(100);
      if (t < T_threshold_low)
      {
        digitalWrite(relay1, HIGH);
        //digitalWrite(vap, HIGH); //i move fan here to check
        Serial.println("Light on");
        Serial.println("fan high");
      }
    }

    


   }
    
