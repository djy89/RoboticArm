# Python Code to test the Game Controller
# Before running this code , make sure you have connected the USB of controller & switched ON the controller 
from Stepper import stepper
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

a1=20  #step servo
a2=20  #step servo
a3=5  #step servo
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
      print("X button pressed s1,s2,s3 left "+str(a1)+" "+str(a2)+" "+str(a3))  #multi threading code
      testStepper = stepper(s)
      testStepper.step(steps, dir,speed);


for device in devices_list:
	if evdev.InputDevice(device).name == "Microsoft X-Box 360 pad":
		print("Index where the Controller is found is : " + str(index))
		break
	else:
		index = index + 1

controller =evdev.InputDevice(devices_list[index])
#print(controller.name)

for event in controller.read_loop():
	if event.code != 0:
		#print(categorize(event))
		#print(event)
		
            if event.code == 17:
                if event.value ==-1:
                    print("top button pressed   S1 right "+str(a1))
                    testStepper1.step(step1, "right",speed1); #steps, dir, speed, stayOn
            if event.code == 17:
                if event.value ==1:
                    print("bottom button pressed  S1 left "+str(a1))
                    testStepper1.step(step1, "left",speed1); #steps, dir, speed, stayOn
            if event.code == 16:
                if event.value ==-1:
                    print("left button pressed   S2 right "+str(a2))
                    testStepper2.step(step2, "right",speed2); #steps, dir, speed, stayOn
            if event.code == 16:
                if event.value ==1:
                    print("right button pressed   S2 left "+str(a2))
                    testStepper2.step(step2, "left",speed2); #steps, dir, speed, stayOn
                    
            if event.code == 307:
                if event.value ==1:
                    print("X button pressed s3 right"+str(a3))
                    testStepper3.step(step3,"right",speed3);
            if event.code == 305:
                if event.value ==1:
                    print("B button pressed s3 left"+str(a3))
                    testStepper3.step(step3,"left",speed3);
                    
                    
            if event.code == 308:
                if event.value == 1:
                    print("Y button pressed S4 left"+str(a4))
                    testStepper4.step(step4,"left",speed4);
		    
            if event.code == 304:
                if event.value == 1:
                    print("A button pressed S4 left"+str(a4))
                    testStepper4.step(step4,"right",speed4);
		    
            if event.code == 310:
                if event.value == 1:
                    print("LB button pressed S4 left"+str(a5))
                    testStepper5.step(step5,"right",speed5);
            if event.code == 311:
                if event.value == 1:
                    print("RB button pressed S4 right"+str(a5))
                    testStepper5.step(step5,"right",speed5);
                    
            
                    
                    
#_thread.start_new_thread( print_time, ("stepper-1", 0.2, s1,angle1,"left",speed1) )
#_thread.start_new_thread( print_time, ("stepper-2", 0.3, s2,angle2,"left",speed2) )
#_thread.start_new_thread( print_time, ("stepper-3", 0.4, s3,angle3,"left",speed3) )
