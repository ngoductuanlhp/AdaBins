import cv2
import os

img_dir = './test_results'

imgs = os.listdir(img_dir)
for img_name in imgs:
    path = os.path.join(img_dir, img_name)

    img = cv2.imread(path, cv2.IMREAD_ANYCOLOR | cv2.IMREAD_ANYDEPTH)
    normed = cv2.normalize(img, None, 0, 255, cv2.NORM_MINMAX, dtype=cv2.CV_8U)
    color = cv2.applyColorMap(normed, cv2.COLORMAP_JET)
    print('Image: ', img_name)
    cv2.imshow('debug', color)
    k = cv2.waitKey(0)
    if k & 0xff == 27:
        break