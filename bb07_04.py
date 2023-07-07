import os
import cv2
from skimage.io import imread, imshow
from matplotlib import pyplot as plt

"하염하염 여기는 수정한 부분 ><"

for i in range(160):
    try:
        x = cv2.imread(f"find(256)/img_{i}.png",0)
        y = cv2.imread(f"find(256)/mask_{i}.png",0)
        p = cv2.imread(f"find(256)/pred_{i}.png",0)

        plt.figure(figsize=(12,8))
        plt.subplot(231)
        plt.imshow(x)
        plt.title("img")

        plt.subplot(232)
        plt.imshow(y)
        plt.title("mask")

        plt.subplot(233)
        plt.imshow(p)
        plt.title("pred")

        plt.show()

    except Exception as e:
        print("Error")


exit()
for i in range(160):
    try:
        x = cv2.imread(f"find(256)/img_{i}.png",0)
        y = cv2.imread(f"find(256)/mask_{i}.png",0)
        p = cv2.imread(f"find(256)/pred_{i}.png",0)

        plt.figure(figsize=(12,8))
        plt.subplot(231)
        plt.imshow(x)
        plt.title("img")

        plt.subplot(232)
        plt.imshow(y)
        plt.title("mask")

        plt.subplot(233)
        plt.imshow(p)
        plt.title("pred")

        plt.show()

    except Exception as e:
        print("Error")

