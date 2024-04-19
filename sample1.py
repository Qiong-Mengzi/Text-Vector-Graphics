# You need cv2 and Numpy to show the TVG image.
import cv2
import numpy as np

import TVG
from TVG.pytvg import TVG_OpenB,TVG_Show

# Open a TVG image
with open('TVG-samples/correct.tvg','r') as f:
    tvg = TVG_OpenB(f.read())

# Create a cloth witch size is your need
cloth = TVG.vEmptyCloth((200,200))

TVG_Show(tvg,cloth)
cv2.imshow('',cv2.cvtColor(np.array(cloth.arr,dtype=np.uint8),cv2.COLOR_RGBA2BGRA))
cv2.waitKey()
cv2.destroyAllWindows()
