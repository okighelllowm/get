import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator

with open('settings.txt') as f:
    sampling_fr, quantization = map(lambda x: float(x[:-2]), f.readlines())

volt, time = [0], [0]
with open('data.txt') as f:
    for i in f:
        adc = int(i)
        volt.append(adc*quantization)
        time.append(time[-1]+1/sampling_fr)
y, x = np.array(volt), np.array(time)

fig = plt.figure(figsize=(16, 9))
ax = plt.axes()
ax.set_title("Процесс заряда конденсатора в RC-цепочкеeeeeeeeeeeeeeeeeeeeeeeeeeeeeee", wrap=True, fontsize=20, verticalalignment='bottom')
plt.plot(x, y, marker='.', markeredgecolor='blue', markersize=5.3, markevery=3, linestyle='-', label='V(t)', color='blue')
plt.xlabel('Время, c')
plt.ylabel('Напряжение, В')
plt.grid(which='major', linestyle='-')
plt.grid(which='minor', linestyle='--')
ax.set_xlim(x.min(), int(x.max())+1)
ax.set_ylim(y.min(), int(y.max())+1)
ax.xaxis.set_major_locator(MultipleLocator(1.000))
ax.xaxis.set_minor_locator(AutoMinorLocator(4))
ax.yaxis.set_major_locator(MultipleLocator(0.500))
ax.yaxis.set_minor_locator(AutoMinorLocator(6))
plt.legend()
plt.annotate(xy=(3, 0.5), text=f'Время зарядки: {"{:.3f}".format(time[-1])}', )
plt.savefig('v(t)_plot.svg')
plt.show()
