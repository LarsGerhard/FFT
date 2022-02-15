from matplotlib.pyplot import plot, legend, show, figure, subplot, title, tight_layout, xlim
from numpy import arange, sin, sqrt, pi, real, imag
from scipy.fftpack import fft

# time dimension

Fs = 500  # Hz  sampling frequency: samples per second
nt = 2000  # number of samples in record
T = nt / Fs  # Time period of record
dT = 1 / Fs  # sec   time between samples

t = arange(0, T, dT)  # time array in seconds using arange(start,stop,step)
#   note that arange actually stops *before* stop time which
#   is what we want (in a periodic function t=0 and t=T are the same)
print(t[0], t[-1], dT)

# frequency dimension

freqf = 1 / T  # Hz   fundamental frequency (lowest frequency)
nfmax = int(nt / 2)  # number of frequencies resolved by FFT

freqmax = freqf * nfmax  # Max frequency (Nyquist)

freq = arange(0, freqmax, 1 / T)  # frequency array using arange(start,stop,step)
# Note:
#     include freq=0 (constant term), so freq[0]=0
#     end one term before the  Nyquist (max) frequency, so freq[-1]=freqmax-freqf

print('Fundamental period and Nyquist Freq', T, freqmax)

# select four frequencies
f1 = 10 * freqf
f2 = freqf
f3 = 2 * freqf
f4 = -5 * freqf

print('Frequencies selected:', f1, f2, f3, f4)

# Create f(t) = A sin(f1 2 pi t) + B sin(f2 2 pi t)  + C cos(f3 2 pi t) + D cos(f4 2 pi t) + E%
# Where A B C D E are integers between -10 and + 10
# Use your time array defined above so f is an array
# with values at each of these times.
# what is the equation for a sine or cos wave with frequency w1?
#    this is an array over all values of time array t, not a "function"
#    sin and cos can opperate on an array so no loop needed
#    remember factor of 2pi
#    basically, just write it like math!
A = -3
B = 5
C = -1
D = 8
E = 6

f = A * sin(f1 * 2 * pi * t) + B * sin(f2 * 2 * pi * t) + C * sin(f3 * 2 * pi * t) + D * sin(f4 * 2 * pi * t) + E

# take FFT of this function
F = fft(f)

# get the coeffs
a = 2 * real(F[:nfmax]) / nt  # form the a coefficients
a[0] = a[0] / 2

b = -2 * imag(F[:nfmax]) / nt  # form the b coefficients

p = sqrt(a ** 2 + b ** 2)  # form power spectrum

# make some plots

figure(1)

subplot(2, 1, 1)
plot(t, f)
title('Signal')

subplot(2, 1, 2)
plot(freq, a, 'o', label='Cosine')
plot(freq, b, '*', label='Sine')
plot(freq, p, '-', label='Power')
legend()

title('FFT Fourier Coefficients')
xmax = max([f1, f2, f3, f4]) * 1.15  # find max value and pad a bit (15%)
xlim(0, xmax)

tight_layout()  # prevent squished plot (matplotlib kludge)

show()
