import RPi.GPIO as GPIO
import time
import random
import matplotlib.pyplot as plt
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
number = [0, 0, 0, 0, 0, 0, 0, 0]
GPIO.setup(dac, GPIO.OUT)

number = [random.randint(0, 1) for i in dac]
GPIO.output(dac, number)

time.sleep(15)
GPIO.output(dac, 0)

GPIO.cleanup(dac)

'''
[0  , 0 , 0 , 0 , 0, 0, 0, 0]
[128, 64, 32, 16, 8, 4, 2, 1]

#for number = 255 number = [1, 1, 1, 1, 1, 1, 1, 1]
#for number = 127 number = [0, 1, 1, 1, 1, 1, 1, 1]
#for number = 64  number = [0, 1, 0, 0, 0, 0, 0, 0]
#for number = 32  number = [0, 0, 1, 0, 0, 0, 0, 0]
#for number = 5   number = [0, 0, 0, 0, 0, 1, 0, 1]
#for number = 0   number = [0, 0, 0, 0, 0, 0, 0, 0]
#for number = 256 number = ???
'''

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT)

dec_numbers = [255, 127, 64, 32, 5, 0]
voltage = []
all_numbers = [ [1, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 1, 1, 1, 1, 1, 1],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 1, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 1, 0, 1],
                [0, 0, 0, 0, 0, 0, 0, 0]]
for number in all_numbers:
    GPIO.output(dac, number)
    volt = float(input('curr volt: '))
    voltage.append(volt)

GPIO.output(dac, 0)
GPIO.cleanup(dac)



fig = plt.figure()
plt.plot(dec_numbers, voltage)
plt.plot(dec_numbers, voltage, 'o')
plt.show()