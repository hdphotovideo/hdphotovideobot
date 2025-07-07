from gfpgan import GFPGANer
import cv2, os

gfpganer = GFPGANer(model_path="GFPGANv1.3.pth", upscale=2, bg_upsampler=None)

def enhance_photo(in_file):
    img = cv2.imread(in_file)
    _, _, restored = gfpganer.enhance(img, has_aligned=False, only_center_face=False)
    out = in_file + "_hd.jpg"
    cv2.imwrite(out, restored)
    return out
