import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)

gpio_out = [2, 3, 4, 17, 27, 22, 10, 9]
GPIO.setup(gpio_out, GPIO.OUT)
GPIO.output(gpio_out, 0)
GPIO.cleanup(gpio_out)