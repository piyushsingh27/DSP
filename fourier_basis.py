import numpy as np
import matplotlib.pyplot as plot

k = 40

time = np.linspace(0, 1, 500)
print(time)

amplitude = 0

for x in range(k + 1):
	z = (2 * x) +1
	amplitude = amplitude + (np.sin(np.pi * 2 * time * z) / z)

print(amplitude)

# plot
plot.plot(time, amplitude)
plot.title('Fourier Basis')
plot.xlabel('Time')
plot.ylabel('Amplitude')
plot.grid(True, which = 'both')
plot.axhline(y = 0, color = 'k')
plot.show()