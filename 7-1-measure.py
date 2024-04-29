import RPi.GPIO as GPIO
import time

def dec2bin(x):
    binary = bin(x)[2::].zfill(8)
    return list(map(lambda x: int(x), binary))

def adc(dac):
    n = len(dac)
    number = 0
    for i in range(n-1, 1, -1):
        number = number | (1 << i)
        signal = dec2bin(number)
        GPIO.output(dac, signal)
        time.sleep(0.01)
        comp_value = GPIO.input(comp)
        if comp_value == 1:
            number = number & ~(1 << i)
    return number

GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13
leds = [2, 3, 4, 17, 27, 22, 10, 9]


GPIO.setup(dac, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(leds, GPIO.OUT, initial=GPIO.LOW)

max_voltage = 3.3
sampling = 2 ** len(dac)
adc_measurments = []
time_measurments = []
volt_measurments = []

try:
    start = time.time() # начало измерений

    # Зарядка конденсатора
    GPIO.output(troyka, GPIO.HIGH)

    digit_volt = adc(dac)
    c_voltage = max_voltage * digit_volt / sampling
    adc_measurments.append(digit_volt)
    volt_measurments.append(c_voltage)
    time_measurments.append(0)

    while c_voltage < (2.3)*0.97:
        digit_volt = adc(dac)
        c_voltage = max_voltage * digit_volt / sampling
        adc_measurments.append(digit_volt)
        volt_measurments.append(c_voltage)
        time_measurments.append(time.time()-start)
        # time.sleep(0.1)

    # Разрядка конденстаора
    '''
    GPIO.output(troyka, GPIO.LOW)

    digit_volt = adc(dac)
    c_voltage = max_voltage * digit_volt / sampling
    volt_measurments.append(c_voltage)
    time_measurments.append(time.time()-start)

    while c_voltage > (2.3)*0.02:
        digit_volt = adc(dac)
        c_voltage = max_voltage * digit_volt / sampling
        volt_measurments.append(c_voltage)
        time_measurments .append(time.time()-start)'''

    end = time.time() # конец измерений
    time = end - start

    # Обработка измерений
    with open('data.txt', 'w') as f:
        for i in range(len(adc_measurments)):
            f.write(f"{adc_measurments[i]}\n")

    with open('settings.txt', 'w') as f:
        average_sampling_fr = len(adc_measurments) / time
        measurment_period = 1/average_sampling_fr
        quantization_step = max_voltage / sampling
        print('Общая продолжительность эксперимента', time)
        print('Период одного измерения', measurment_period)
        f.write(str(average_sampling_fr)+'\n')
        print('Средняя частота дискретизации:', average_sampling_fr)
        f.write(str(quantization_step)+'\n')
        print('Шаг квантования АЦП:', quantization_step)
finally:
    GPIO.output(dac, GPIO.LOW)
    GPIO.cleanup()
    print('end.')