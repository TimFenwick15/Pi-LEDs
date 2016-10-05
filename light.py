import time
import RPi.GPIO as GPIO

pin = 47
#pin = 35
if pin == 35:
  colour = "red"
else:
  colour = "green"

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(pin, GPIO.OUT)


while True:
  GPIO.output(pin, GPIO.HIGH)

print("Turning off {} Light".format(colour))
GPIO.output(pin, GPIO.LOW)

time.sleep(5)

print("Turning on {} Light".format(colour))
GPIO.output(pin, GPIO.HIGH)

time.sleep(5)

print("Turning off {} Light".format(colour))
GPIO.output(pin, GPIO.LOW)

time.sleep(5)

print("Turning on {} Light".format(colour))
GPIO.output(pin, GPIO.HIGH)

GPIO.cleanup()
