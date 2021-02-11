import cv2
import os
from glob import glob


png=glob("C:/YOLO/custom_yolo_model/spot_data/spot_images/*png")

for j in png:
    print(j)
    img=cv2.imread(j)
    cv2.imwrite(j[:-3]+"jpg",img)
    os.remove(j)
