import RPi.GPIO as GPIO
import datetime
import time
from sys import argv

on_for = argv[1]
off_for = argv[2]

# on_for = raw_input("Please enter the seconds it should be on for? ")
# off_for = raw_input("Please enter the seconds it should be off for? ")

while True:
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(18,GPIO.OUT)
    print "LED on",time.strftime('%X %x %Z')
    GPIO.output(18,GPIO.HIGH)
    time.sleep(float(on_for))
    print "LED off", time.strftime('%X %x %Z')
    GPIO.output(18,GPIO.LOW)
    time.sleep(float(off_for))
    if False:
      break

