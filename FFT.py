n = 200
x=np.linspace(0,2*np.pi,n)
f=np.exp(-2*(x-np.pi)*(x-np.pi))*np.cos(3*x)
ft=np.fft.fft(f)
ftp=fftshift(abs(ft))