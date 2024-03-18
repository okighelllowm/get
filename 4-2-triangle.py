import RPi.GPIO as GPIO
import time

def dec2bin(x):
    binary = bin(x)[2::].zfill(8)
    return list(map(lambda x: int(x), binary))

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)

sampling = 2 ** len(dac)
try:
    T = int(input('enter time of period: '))
    t = T / (2 * sampling)

    while True:
        for x in range(256):
            GPIO.output(dac, dec2bin(x))

            time.sleep(t)

        for x in range(255, 0, -1):
            GPIO.output(dac, dec2bin(x))

            time.sleep(t)

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
    print('end.')