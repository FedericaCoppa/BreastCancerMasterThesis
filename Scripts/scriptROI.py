import os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
from PIL import Image
import PIL

path_roi = '/media/federica/Loserino/CBIS-DDSM/CalcTrainingROI/PNGOutput/'
path_img = '/media/federica/Loserino/CBIS-DDSM/CalcTrain/PNGOutput/'

path_out = '/media/federica/Loserino/CBIS-DDSM/path_out/'


def bbox1(img):
    a = np.where(img != 0)
    bbox = np.min(a[0]), np.max(a[0]), np.min(a[1]), np.max(a[1])
    return bbox 

for f in os.listdir(path_roi):
    print(f)
    try:
        roi = plt.imread(path_roi + f)
        img = plt.imread(path_img + f)
    except FileNotFoundError:
        continue
    if roi.shape != img.shape:
        continue
    my, My, mx, Mx = bbox1(roi)
    crop = img[my:My, mx:Mx]
    plt.imsave(path_out + f, crop, cmap='gray')
    

