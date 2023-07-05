# -*- coding: utf-8 -*-
"""imageprocessing_CLAHE&THRESHOLDING.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1cFlQTmFeLIUqfDyBlfy5einC2qA4p_V_

**CLACHE & THRESHOLDING**
"""

import cv2
import numpy as np
from matplotlib import pyplot as plt
from google.colab.patches import cv2_imshow

img = cv2.imread("/content/denoise.jpeg", 0)
equ = cv2.equalizeHist(img)

plt.hist(equ.flat, bins=100, range=(0,100))

cv2_imshow( img)
cv2_imshow( equ)
clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))  #Define tile size and clip limit.
cl1 = clahe.apply(img)

cv2_imshow( cl1)

cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/content/denoise.jpeg", 0)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))  #Define tile size and clip limit.
clahe_img = clahe.apply(img)
plt.hist(clahe_img.flat, bins =100, range=(0,255))

from google.colab.patches import cv2_imshow
ret,thresh1 = cv2.threshold(clahe_img,185,150,cv2.THRESH_BINARY)  #All thresholded pixels in grey = 150
ret,thresh2 = cv2.threshold(clahe_img,185,255,cv2.THRESH_BINARY_INV) # All thresholded pixels in white

cv2_imshow( img)
cv2_imshow(thresh1)
cv2_imshow(thresh2)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import matplotlib.pyplot as plt
from google.colab.patches import cv2_imshow

img = cv2.imread("/content/denoise.jpeg", 0)

clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))  #Define tile size and clip limit.
clahe_img = clahe.apply(img)

plt.hist(clahe_img.flat, bins =100, range=(0,255))
ret1,th1 = cv2.threshold(clahe_img,185,200,cv2.THRESH_BINARY)

ret2,th2 = cv2.threshold(clahe_img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2_imshow(th2)
cv2.waitKey(0)
cv2.destroyAllWindows()

import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/content/denoise.jpeg", 0)

blur = cv2.GaussianBlur(clahe_img,(5,5),0)
ret3,th3 = cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


plt.hist(blur.flat, bins =100, range=(0,255))
cv2_imshow(th3)
cv2.waitKey(0)
cv2.destroyAllWindows()