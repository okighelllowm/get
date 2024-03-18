import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(21, GPIO.OUT)

p = GPIO.PWM(21, 100)

max_voltage = 3.3
try:
    while True:
        dc = int(input('enter duty cycle: '))
        p.start(dc)
        print("{:.4f}".format(dc * max_voltage / 100))
        quit = input('Press return to stop:')
        p.stop()
        if quit == 'q':
            break
finally:
    GPIO.cleanup()