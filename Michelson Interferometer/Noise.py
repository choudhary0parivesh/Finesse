#%%

import numpy as np
import matplotlib.pyplot as plt
import scipy.signal as sig


plt.style.use('fivethirtyeight')
plt.rcParams['lines.linewidth'] = 3
plt.rcParams['font.size'] = 22
plt.rcParams['axes.titlesize']  = 'large'
plt.rcParams['axes.labelsize']  = 'large'
plt.rcParams['xtick.labelsize'] = 'large'
plt.rcParams['ytick.labelsize'] = 'large'
plt.rcParams['axes.formatter.limits'] = [-2,2]
plt.rcParams['axes.grid'] = True
plt.rcParams['grid.linestyle'] = '--'
plt.rcParams['grid.linewidth'] = 0.7
plt.rcParams['grid.alpha'] = 0.4
plt.rcParams['text.usetex'] = False
plt.rcParams['legend.loc'] = 'best'
plt.rcParams['legend.fontsize'] = 'small'
plt.rcParams['figure.figsize'] = [12,9]
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['figure.subplot.left'] = 0.07
plt.rcParams['figure.subplot.right'] = 0.95
plt.rcParams['figure.subplot.top'] = 0.92


def rms_timeDomain(V):
    Vsq = V**2
    return(np.sqrt(np.mean(Vsq)))

def cum_rms(ff, asd):
    
    df = np.roll(ff, -1) - ff
    df = df[:-1]
    cum_ms = np.zeros(len(ff))
    for ii in range(len(cum_ms)):
        cum_ms[ii] = np.trapz(asd[ii:]**2, ff[ii:])
    return(cum_ms**0.5)


fs = 100                            
tDur = 10                           
nSamples = int(10 / (1/fs) + 1)      
t = np.linspace(0,tDur,nSamples)   
Vn = np.random.randn(int(nSamples)) 
Vrms = rms_timeDomain(Vn)          
print('The RMS value of the signal is {}'.format(round(Vrms,3)))


# FFT parameters
t_fft = 1                                 
nFFT = int(t_fft * fs)                      
win = sig.get_window(('tukey',0.25), nFFT)  


# Do the FFT
ff, Pxx = sig.welch(Vn, fs=fs, window=win, 
                    scaling='density')
rms_f = cum_rms(ff, np.sqrt(Pxx))


# Make a plot
fig, ax = plt.subplots(1,1,figsize=(16,9))
ax.loglog(ff, np.sqrt(Pxx), label='ASD', 
          color='xkcd:bright blue',
         rasterized=True, linewidth=3, alpha=0.7)
ax.loglog(ff, rms_f, linestyle='--', 
          color='xkcd:bright blue', alpha=0.7,
         rasterized=True, linewidth=3, label='RMS')
ax.legend(loc='best')
ax.set_xlabel('Frequency [Hz]')
ax.set_ylabel('ASD [$\\frac{\\mathrm{a.u.}}{\\sqrt{\\mathrm{Hz}}}$]')
fig.suptitle('ASD of simulated Gaussian white noise');
print('The RMS value computed from the frequency domain is {} a.u.'.format(round(rms_f[0],3)))
print('That from the time domain calculation was {} a.u.'.format(round(Vrms,3)))
