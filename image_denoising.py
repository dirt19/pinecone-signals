import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as img
from skimage.color import rgb2gray
from skimage import io

# apply noise
A=io.imread('photo.jpeg')
Abw = rgb2gray(A)
B=Abw+0.5*np.random.randn(600,800)
Bt=np.fft.ftt2(B)
Bts=fftshift(Bt)

# low-pass notch filter
Fs=np.zeros((600,800))
width=50
mask=np.ones((2*width+1,2*width+1))
Fs[301-width:301+width+1,401-width:401+width+1]=mask
Btfs=np.multiply(Bts,Fs)
Btf=fftshift(Btsf)
Bf=np.fft.ifft2(Btf)