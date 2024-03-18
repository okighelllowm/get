import RPi.GPIO as GPIO

def signal_on_dac(x):
    binary = bin(x)[2::].zfill(8)
    return list(map(lambda x: int(x), binary))

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)

max_voltage = 3.3
sampling = 2 ** len(dac)

try:
    while True:
        number = input('enter integer number between 0 and 255: ')
        if number == 'q':
            break
        
        if not number.isdigit():
            print(f"{number} should be int. try again")
        elif int(number) < 0 or int(number) > 255:
            print(f"{number} is out of range. try again")
        else:
            number = int(number)
            GPIO.output(dac, signal_on_dac(number))

            volt = max_voltage * number / sampling
            print('current voltage on dac:', "{:.4f}".format(volt))

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup(dac)
    print('end.')
