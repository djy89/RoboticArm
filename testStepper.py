from Stepper import stepper



testStepper = stepper([10, 9, 11])  #[stepPin, directionPin, enablePin]
testStepper.step(360*19, "left",0.005); #steps, dir, speed, stayOn


