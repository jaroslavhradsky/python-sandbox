# Incorporation of NumPy with OpenCV

import numpy as np
import cv2

# 256x256 pixel array with a horizontal gradient from 0 to 255 for the red color channel
r = np.reshape(np.arange(256*256)%256,(256,256))  

# array of same size and type as r but filled with 0s for the green color channel
g = np.zeros_like(r)  

# transposed r will give a vertical gradient for the blue color channel
b = r.T 

# OpenCV images are interpreted as BGR, the depth-stacked array will be written to an 8bit RGB PNG-file called 'gradients.png'
cv2.imwrite('gradients.png', np.dstack([b,g,r]))  