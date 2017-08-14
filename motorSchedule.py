import RPi.GPIO as GPIO
import datetime
import time
from sys import argv
from time import sleep

on_for = argv[1]
off_for = argv[2]

# on_for = raw_input("Please enter the seconds it should be on for? ")
# off_for = raw_input("Please enter the seconds it should be off for? ")


GPIO.setmode(GPIO.BOARD)

Motor1A = 16
Motor1B = 18
Motor1E = 22

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)


while True:
    print "Motor on",time.strftime('%X %x %Z')
    GPIO.output(Motor1A,GPIO.HIGH)
    GPIO.output(Motor1B,GPIO.LOW)
    GPIO.output(Motor1E,GPIO.HIGH)
    time.sleep(float(on_for))
    print "Motor off", time.strftime('%X %x %Z')
    GPIO.output(Motor1E,GPIO.LOW)
    time.sleep(float(off_for))
    if False:
      break




print "Turning motor on"
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)

sleep(2)

