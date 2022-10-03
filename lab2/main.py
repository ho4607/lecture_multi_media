import cv2 
import numpy as np
from PIL import Image  # pillow
from matplotlib import pyplot as plt
import sys

from helper import makeRandomOneZeroMatrix1024by1024

im1 = cv2.imread('./data/IMG_3376_trimmed.png',0)

# random matrix 1024 by 1024, composed of 0 and 1
matrix, opp_matrix = makeRandomOneZeroMatrix1024by1024()
set1 = im1*matrix
set2 = im1*opp_matrix

# image save
plt.imsave('./result/set1.png',set1,cmap='gray')
plt.imsave('./result/set2.png',set2,cmap='gray')

set1_plus_5 = np.clip((set1+5)*matrix,0,255)
set2_subtract_5 = np.clip((set2-5)*opp_matrix,0,255)

s1=(np.abs(set1.sum()-set2.sum()))/2**19
s2=(set1_plus_5.sum()-set2_subtract_5.sum())/2**19

# image save
plt.imsave('./result/set1_plus_5.png',set1_plus_5,cmap='gray')
plt.imsave('./result/set2_subtract_5.png',set2_subtract_5,cmap='gray')

# combine image
comb_img = set1_plus_5+set2_subtract_5
plt.imsave('./result/comb_img.png',comb_img,cmap='gray')

# random matrix 1024 by 1024, composed of 0 and 1
matrix2, opp_matrix2 = makeRandomOneZeroMatrix1024by1024()
set3 = comb_img*matrix2
set4 = comb_img*opp_matrix2

s3=(np.abs(set3.sum()-set4.sum()))/2**19


print("random vector")
print(matrix)
print("not gated random vector")
print(opp_matrix)
print('----------')
print('set1')
print(set1)
print('set2')
print(set2)
print('-----------')
print('max, min check')
print(set1_plus_5.max(), set1_plus_5.min())
print(set2_subtract_5.max(), set2_subtract_5.min())

print('-----')
print('s1:',s1)
print('s2:',s2)
print('s3:',s3)
