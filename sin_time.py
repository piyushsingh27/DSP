import numpy as np
import matplotlib.pyplot as plot

# init
time = np.arange(0, 10, 0.1) # np.aragne(start, stop, step)
print(time)
amplitude = np.sin(time)
print(amplitude)

# plot
plot.plot(time, amplitude)
plot.title('Sine wave')
plot.xlabel('Time')
plot.ylabel('Amplitude = sin(time)')
plot.grid(True, which = 'both')
plot.axhline(y = 0, color = 'k')
plot.show()
