#include <Stepper.h>

const int spr = 1600;  // change this to fit the number of steps per revolution

int a1,a2,a3; //angles
float g1,g2,g3; // gear ratios
float s1,s2,s3; // number of steps
float c1,c2,c3; // count the number of steps
int d1,d2,d3; // Direction parameter
String ss; char s; int ss1=0; int ss2=0; int ss3=0; // String parsing parameters for getting 3 angles
int r=0; // Run Stepper Flag

// initialize the stepper library on pins 8 through 11:
Stepper myStepper1(spr, 2, 3, 4, 5);
Stepper myStepper3(spr, 6, 7, 8, 9);
Stepper myStepper2(spr, 10, 11, 12, 13);

void setup() 
{ // set the speed at 60 rpm:
  myStepper1.setSpeed(100); myStepper2.setSpeed(100); myStepper3.setSpeed(100);
  // initialize the serial port:
  Serial.begin(115200); 
//  a1=5;
//  a2=2;
//  a3=10;

// gear ratios
  g1=110/9;
  g2=10;
  g3=10;

// Steps for each stepper
  s1=(spr/360)*a1*g1;  
  s2=(spr/360)*a2*g2;  
  s3=(spr/360)*a3*g3;

}


void loop() 
{
  // Get angle for joint 1
  s=Serial.read();
  if(s == 'a')
   { while (1)  {
          s = Serial.read();  if (s == '\n') break;
          ss = ss + s;
              }

  ss1=ss.toInt();
  //Serial.println(ss1);
  }
  
// Get angle for joint 2
if(s == 'b')
   { while (1)  {
          s = Serial.read();  if (s == '\n') break;
          ss = ss + s;
              }

  ss2=ss.toInt();
  //Serial.println(ss2);
  }
  
// Get angle for joint 3
if(s == 'c')
   { while (1)  {
          s = Serial.read();  if (s == '\n') break;
          ss = ss + s;
              }

  ss3=ss.toInt();
  //Serial.println(ss3);
  }

// Get run command
if(s == 'r')
   { while (1)  {
          s = Serial.read();  if (s == '\n') break;
          ss = ss + s;
              }

  r=ss.toInt();
  //Serial.println(r);
  }
// Direction for each stepper corresponding to serial input
if(a1>0) d1=1; else d1=-1;
if(a2>0) d2=1; else d2=-1;
if(a3>0) d3=-1; else d3=1; // Signs reversed coz of mechanical constraint

a1=ss1; a2=ss2; a3=ss3;



Serial.print("a1- "); Serial.print(a1);  Serial.print("  a2- "); Serial.print(a2); Serial.print("  a3- "); Serial.println(a3);

// Angles to steps
s1=(spr/360)*a1*g1; 
s2=(spr/360)*a2*g2;  
s3=(spr/360)*a3*g3;

// Sequence to run all the steppers by the command 'r1' in serial monitor
 
while(r==1){
  Serial.print("Running-->  ");
 
 if(abs(s1)>c1){myStepper1.step((spr/360)*d1); c1++; Serial.print(d1); Serial.print(" stepper1- "); Serial.print(c1);Serial.print("   ");}
 if(abs(s2)>c2){myStepper2.step((spr/360)*d2); c2++; Serial.print(d2); Serial.print(" stepper2- "); Serial.print(c2);Serial.print("   ");}
 if(abs(s3)>c3){myStepper3.step((spr/360)*d3); c3++; Serial.print(d3); Serial.print(" stepper3- "); Serial.print(c3); }
  Serial.println(); 
 if(abs(s1)<=c1 && abs(s2)<=c2 && abs(s3)<=c3) {Serial.println("DONE"); r=0; break;} // Check for completion of all the 3 steppers and breaks the loop.
}
 
//----------
ss = "";   c1=0; c2=0; c3=0; r=0;  // Resetting counters, serial buffer and run flag.
delay(10); 

}
 
