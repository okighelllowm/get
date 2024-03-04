import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(leds, GPIO.OUT)

GPIO.output(leds, 0)

for i in range(3):
    for led in leds:
        GPIO.output(led, 1)
        time.sleep(0.5)
        GPIO.output(led, 0)

GPIO.output(leds, 0)

GPIO.cleanup(leds)