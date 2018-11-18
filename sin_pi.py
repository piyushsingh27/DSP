import numpy as np
import matplotlib.pyplot as plot

# init
angle = np.linspace(0, 2 * np.pi, 200) # np.linspace(start, stop, no. samples)
print(angle)
amplitude = np.sin(angle)
print(amplitude)

# plot
plot.plot(angle, amplitude)
plot.title('Sine wave')
plot.xlabel('Angle')
plot.ylabel('Amplitude = sin(time)')
plot.grid(True, which = 'both')
plot.axhline(y = 0, color = 'k')
plot.show()
