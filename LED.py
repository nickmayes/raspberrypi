import RPi.GPIO as GPIO
import time

while True:




    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    print "LED on"
    GPIO.output(18,GPIO.HIGH)
    time.sleep(10)
    print "LED off"
    GPIO.output(18,GPIO.LOW)
    time.sleep(3)
    if False:
      break
