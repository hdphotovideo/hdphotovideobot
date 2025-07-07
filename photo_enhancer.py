import cv2
import os

def enhance_photo(in_file):
    img = cv2.imread(in_file)
    height, width = img.shape[:2]
    upscaled = cv2.resize(img, (width*2, height*2), interpolation=cv2.INTER_CUBIC)
    out = in_file + "_hd.jpg"
    cv2.imwrite(out, upscaled)
    return out
