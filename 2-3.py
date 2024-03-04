import RPi.GPIO as GPIO
# import time
GPIO.setmode(GPIO.BCM)

leds = [2, 3, 4, 17, 27, 22, 10, 9]
aux = [21, 20, 26, 16, 19, 25, 23, 24]
GPIO.setup(leds, GPIO.OUT)
GPIO.setup(aux, GPIO.IN)

for i in range(8):
    signal = GPIO.input(aux[i])
    GPIO.output(leds[i], signal)

while True:
    signals = []
    for i in range(8):
        signal = GPIO.input(aux[i])
        GPIO.output(leds[i], signal)
        signals.append(signal)
    if signals == [0, 0, 1, 1, 1, 1, 1, 1]:
        break

GPIO.output(leds, 0)
GPIO.cleanup(leds)
GPIO.cleanup(aux)
