from math import log10, sqrt
import cv2
import numpy as np

def calculate_psnr(source, compressed):
    mse = np.mean((source - compressed)**2)
    if(mse == 0):
        return 100
    max_pixel = 255.0
    psnr = 20*log10(max_pixel/sqrt(mse)) 
    return psnr
    