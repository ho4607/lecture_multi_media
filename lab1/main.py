from PIL import Image  # pillow
import numpy as np
from matplotlib import pyplot as plt
import cv2

from img_process import trim, decompose_mag_pha
from psnr import calculate_psnr

# Load images
im1 = cv2.imread('./data/IMG_3084.JPG',0)
im2 = cv2.imread('./data/IMG_3376.JPG',0)

# Trim the images to 1024 by 1024
im1_trimmed = trim(im1, 1000, 2000, 1024, 1024)
im2_trimmed = trim(im2, 0, 0, 1024, 1024)

print(im1_trimmed.shape)
print(im2_trimmed.shape)

# save trimmed images
Image.fromarray(im1_trimmed).save('./result/trimmed_img/IMG_3084_trimmed.JPG')
Image.fromarray(im2_trimmed).save('./result/trimmed_img/IMG_3376_trimmed.JPG')

# decompose magnitude and phase spectrum from im1
im1_decomposed = decompose_mag_pha(im1_trimmed)
im1_fft = im1_decomposed['fft']
im1_magnitude_spectrum = im1_decomposed['mag_spec']
im1_phase_spectrum = im1_decomposed['pha_spec']

# decompose magnitude and phase spectrum from im2
im2_decomposed = decompose_mag_pha(im2_trimmed)
im2_fft = im2_decomposed['fft']
im2_magnitude_spectrum = im2_decomposed['mag_spec']
im2_phase_spectrum = im2_decomposed['pha_spec']

# Save their spectrum as image
plt.imsave('./result/spectrum/IMG_3084_dft_mag.JPG',im1_magnitude_spectrum,cmap='gray')
plt.imsave('./result/spectrum/IMG_3084_dft_phase.JPG',im1_phase_spectrum,cmap='gray')

plt.imsave('./result/spectrum/IMG_3376_dft_mag.JPG',im2_magnitude_spectrum,cmap='gray')
plt.imsave('./result/spectrum/IMG_3376_dft_phase.JPG',im2_phase_spectrum,cmap='gray')

# Exchange their phase component
combined_mag_im1_pha_im2 = np.multiply(np.abs(im1_fft), np.exp(1j*np.angle(im2_fft)))
imgCombined1 = np.real(np.fft.ifft2(combined_mag_im1_pha_im2))

combined_mag_im2_pha_im1 = np.multiply(np.abs(im2_fft), np.exp(1j*np.angle(im1_fft)))
imgCombined2 = np.real(np.fft.ifft2(combined_mag_im2_pha_im1))

# Save exchanged reconstruction images
plt.imsave('./result/exchanged_reconstruction/combined_mag_im1_pha_im2.JPG',imgCombined1,cmap='gray')
plt.imsave('./result/exchanged_reconstruction/combined_mag_im2_pha_im1.JPG',imgCombined2,cmap='gray')

# Calculate PSNR 
psnr_im1_comb2=calculate_psnr(im1_trimmed, imgCombined2)
psnr_im2_comb1=calculate_psnr(im2_trimmed, imgCombined1)
print('psnr_im1_comb2:',psnr_im1_comb2,", psnr_im2_comb1:",psnr_im2_comb1 )