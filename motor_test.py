# Krystal Kwan
# 1/2/2017

import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

#Motor1A = 16
Motor1A = 33

#Motor1B = 18
Motor1B = 35

#Motor1E = 22
Motor1E = 37

GPIO.setup(Motor1A,GPIO.OUT)
GPIO.setup(Motor1B,GPIO.OUT)
GPIO.setup(Motor1E,GPIO.OUT)

print("Turning motor on")
GPIO.output(Motor1A,GPIO.HIGH)
GPIO.output(Motor1B,GPIO.LOW)
GPIO.output(Motor1E,GPIO.HIGH)

sleep(2)

print("Stopping motor")
GPIO.output(Motor1E,GPIO.LOW)

GPIO.cleanup()
