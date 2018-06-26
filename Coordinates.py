# Python Code to test the Game Controller
# Before running this code , make sure you have connected the USB of controller & switched ON the controller 
from Stepper import stepper
import math
import evdev
import _thread
import time
from evdev import InputDevice, categorize, ecodes
import RPi.GPIO as GPIO
 ################## Gear ratios
g1 = 12.22
g2 = 10
g3 = 10
 
 ################# pulses/ rev
ppr=1600
 
 ##################rpi gpio for steppers

s1=[2,3,4]     #3,5,7
s2=[17,27,22]  #11,13,15
s3=[10,9,11]   #19,21,23
s4=[5,6,13]    #29,31,33
s6=[25,8,7]    #22,24,26
s5=[16,20,21]  #36,38,40

 ########## Stepper Objects

testStepper1 = stepper(s1)
testStepper2 = stepper(s2)
testStepper3 = stepper(s3)
testStepper4 = stepper(s4)
testStepper5 = stepper(s5)
testStepper6 = stepper(s6)

 ############ minimum angle rotation
l1=420
l2=10
l3=10


a1=10  #step servo
a2=10  #step servo
a3=10  #step servo
a4=20
a5=20
a6=20

# Converting Angles to steps

step1=(ppr/360)*a1*g1  #Step Servo 400steps/rev
#step1=(360/a1)*(200/ppr)*g1  #Step Servo 400steps/rev
speed1=0.01

step2=(ppr/360)*a2*g2   #Step Servo 400steps/rev
speed2=0.01

step3=(ppr/360)*a3*g3    #Step Servo 400steps/rev
speed3=0.01

step4=a4*19*0.55555
speed4=0.005

step5=a5
speed5=0.001

step6=100
speed6=0.001



devices_list = evdev.list_devices() # This would give us the list of devices 
index = 0

"""
InputDevice gives the device type which has following properties :
1.name
2.capbilities
3.phys


Event has following properties mainly : 
1.Code
2.type 
3.Value



"""
def print_time( threadName, delay,s,steps, dir,speed):
   count = 1
   while count >=1:
      time.sleep(delay)
      count -= 1
      #print ("%s: %s" % ( threadName, time.ctime(time.time()) ))
      #print("X button pressed s1,s2,s3 left "+str(a1)+" "+str(a2)+" "+str(a3))  #multi threading code
      testStepper = stepper(s)
      testStepper.step(steps, dir,speed);

########coordinates in xy frame

x=5
y=5

#######Inverse Kinematics Equation for obtaining th joint angles
theta3=math.acos((x*x+y*y-(l1*l1)-(l2*l2))/(2*l1*l2))
theta2=math.atan((y*(l1+l2*math.cos(theta3))-(x*l2*math.sin(theta3)))/(x*(l1+l2*math.cos(theta3))+(y*l2*math.sin(theta3))))
theta1=math.atan(y/x)

print(str(theta1)+" "+str(theta2)+ " "+str(theta3))
                    
          
                    
#######MultiThreading Sequence                   
_thread.start_new_thread( print_time, ("stepper-1", 0.2, s1,theta1,"left",speed1) )
_thread.start_new_thread( print_time, ("stepper-2", 0.3, s2,theta2,"left",speed2) )
_thread.start_new_thread( print_time, ("stepper-3", 0.4, s3,theta3,"left",speed3) )

