import numpy as np


def trim(array, x, y, width, height):
    return array[y:y+height, x:x+width]


def decompose_mag_pha(img):
    fft = np.fft.fft2(img)
    fft_shift = np.fft.fftshift(fft)
    magnitude_spectrum = 20*np.log(abs(fft_shift))
    phase_spectrum = np.angle(fft_shift)
    return {"mag_spec":magnitude_spectrum,"pha_spec": phase_spectrum, 'fft':fft}