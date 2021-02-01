void setup() {
  Serial.begin(9600);
  pinMode(2, INPUT_PULLUP);
  pinMode(4, INPUT_PULLUP);
  pinMode(7, INPUT_PULLUP);
  pinMode(8, INPUT_PULLUP);
  pinMode(12, INPUT_PULLUP);
  pinMode(6,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(3,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  digitalWrite(6,LOW);
  digitalWrite(5,LOW);
  digitalWrite(3,LOW);
  digitalWrite(9,LOW);
  digitalWrite(10,LOW);
  digitalWrite(11,LOW);
    
}
int Img_Recog = 1;
int Add = 1;
int Remove = 1;
int Change = 1;
int No_plate = 1;
String data_read;

void loop() {
  
  int pinValue = digitalRead(2);
  delay(5);
  
  if (Img_Recog != pinValue){
    Img_Recog = pinValue;
    if (Img_Recog==1){
      Serial.println(1);
    }
  }
 int pinValue1 = digitalRead(4);
  delay(5);
  if (Add !=pinValue1){
    Add = pinValue1;
    if (Add == 0){
      Serial.println(12341);
    }
  }
  int pinValue2 = digitalRead(7);
  delay(5);
  if (Remove !=pinValue2){
    Remove = pinValue2;
    if (Remove == 0){
      Serial.println(12342);
    }
  }
  int pinValue3 = digitalRead(8);
  delay(5);
  if (Change !=pinValue3){
    Change = pinValue3;
    if (Change == 0){
      Serial.println(12343);
    }
  }
  int pinValue4 = digitalRead(12);
  delay(5);
  if (No_plate !=pinValue4){
    No_plate = pinValue4;
    if (No_plate == 0){
      Serial.println(12);
    }
  }

while (Serial.available()>0)
  {
    data_read = Serial.readStringUntil('\n');
  }
 if (data_read == "20"){  
  digitalWrite (10, HIGH); }
  else if (data_read == "21"){
  digitalWrite(10,LOW); 
  }
  else if (data_read == "10"){  
  digitalWrite (9, HIGH); }
  else if (data_read == "11"){
  digitalWrite(9,LOW); 
  }

  else if (data_read == "100"){  
  digitalWrite (3, HIGH); }
  else if (data_read == "101"){
  digitalWrite(3,LOW); 
  }
  else if (data_read == "1000"){
  digitalWrite (5, HIGH);}
  else if (data_read == "1001"){
  digitalWrite(5,LOW);
  }
  else if (data_read == "10000"){
  digitalWrite (6, HIGH);

  }
  else if (data_read =="10001"){
    digitalWrite(6,LOW);
  }
  }
