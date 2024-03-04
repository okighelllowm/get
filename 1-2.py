import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

channel = 17

GPIO.setup(channel, GPIO.OUT)
GPIO.output(channel, 0)

for i in range(5):
    GPIO.output(channel, 1)
    time.sleep(1)
    GPIO.output(channel, 0)
    time.sleep(1)

GPIO.output(channel, 0)
GPIO.cleanup(channel)