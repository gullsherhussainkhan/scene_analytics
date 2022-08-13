import numpy as np
from cv2 import mean as cv2_mean
from cv2 import rectangle as cv2_rectangle


class BlurRegion: 

    def extract_region(self,input_image,start_y,end_y,start_x,end_x):
        return input_image[start_y:end_y,start_x:end_x]
    
    def gaussian_blur(self,input_region, blocks=10):
    
        (h, w) = input_region.shape[:2]

        x = np.linspace(0, w, blocks + 1, dtype="int")
        y = np.linspace(0, h, blocks + 1, dtype="int")

        for i in range(1, len(y)):
            for j in range(1, len(x)): 
                startX = x[j - 1]
                startY = y[i - 1]
                endX = x[j]
                endY = y[i]

                region_of_interest = input_region[startY:endY, startX:endX]
                (B, G, R) = [int(x) for x in cv2_mean(region_of_interest)[:3]]

                cv2_rectangle(input_region, (startX, startY), (endX, endY),(B, G, R), -1)

        return input_region


    