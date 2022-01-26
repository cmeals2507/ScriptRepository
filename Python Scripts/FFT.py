import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
from scipy.fft import irfft
import numpy as np
rate, data = wav.read('/Users/corymeals/Desktop/University of Houston 4.wav')
new_sig = irfft(data)
#fft_out = fft(data)
#%matplotlib inline
#plt.plot(data, np.abs(fft_out))
plt.plot(new_sig[:250])
plt.show()