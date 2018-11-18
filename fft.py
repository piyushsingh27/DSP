import numpy as np
import matplotlib.pyplot as plot
import scipy.fftpack as fft

# sample space
T = 1.0 / 800.0

# no of samples
N = 600

# original data
x = np.linspace(0, N * T, N)
y = np.sin(40.0 * 2.0 * np.pi * x) + (0.5 * np.sin(90.0 * 2.0 * np.pi * x))

# fast fourier transform
xf = np.linspace(0, 1.0 / T, N)
yf = fft.fft(y);

# plot
p1 = plot.figure(1)
plot.plot(x, y)
plot.title('Input Data')
plot.xlabel('Time')
plot.ylabel('Amplitude');
plot.grid(True, which = 'both')
plot.axhline(y = 0, color = 'k')
p1.show()

p2 = plot.figure(2);
plot.plot(xf[:N // 2], 2.0 / N * np.abs(yf[:N // 2]))
plot.title('Fast Fourier Transform')
plot.xlabel('Time')
plot.ylabel('Amplitude');
plot.grid(True, which = 'both')
plot.axhline(y = 0, color = 'k')
p2.show()

input()