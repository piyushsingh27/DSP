import numpy as np
import matplotlib.pyplot as plot

def dft(x):
	N = x.size
	n = np.arange(N)
	k = n.reshape((N, 1))
	e = np.exp(-2j * np.pi * k * n / N)
	return np.dot(e, x)

# sample space
T = 1.0 / 800.0

# no of samples
N = 600

# original data
x = np.linspace(0, N * T, N)
y = np.sin(40.0 * 2.0 * np.pi * x) + (0.5 * np.sin(90.0 * 2.0 * np.pi * x))

# fast fourier transform
xf = np.linspace(0, 1.0 / T, N)
yf = dft(y);

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