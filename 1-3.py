import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

gpio_out = 17
gpio_in = 22

GPIO.setup(gpio_in, GPIO.IN)
GPIO.setup(gpio_out, GPIO.OUT)
GPIO.output(gpio_out, 0)

signal = GPIO.input(gpio_in)
GPIO.output(gpio_out, signal)
time.sleep(5)

GPIO.output(gpio_out, 0)
GPIO.cleanup((gpio_in, gpio_out))