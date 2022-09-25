import cv2 
import numpy as np
from PIL import Image  # pillow
from matplotlib import pyplot as plt

from helper import shuffle_2D_matrix

im1 = cv2.imread('./data/IMG_3376_trimmed.png',0)

# random matrix 1024 by 1024
ran2d = np.zeros(2**20)
ran2d[:2**19] = 1
np.random.shuffle(ran2d)
ran2d = ran2d.reshape(1024,1024)

t_ran2d = np.logical_not(ran2d)*1

# separate image as set1, set2
set1 = im1*ran2d
set2 = im1*t_ran2d

# image save
plt.imsave('./result/set1.png',set1,cmap='gray')
plt.imsave('./result/set2.png',set2,cmap='gray')

s1=(set1.sum()-set2.sum())/2**19

print("random vector")
print(ran2d)
print("not gated random vector")
print(t_ran2d)
print('set1')
print(set1)
print('set2')
print(set2)
print(s1)
print(ran2d.sum())
