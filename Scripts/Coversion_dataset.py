import numpy as np
import pydicom
from PIL import Image
import os

def get_names(path): #path lavora in directory corrente
    names = []
    for root, dirnames, filenames in os.walk(path):
        for filename in filenames:
            _, ext = os.path.splitext(filename)
            if ext in ['.dcm']:
                names.append(filename)
    return names

def convert_dcm_png(name): #converte in png

    im = pydicom.dcmread(name)

    im = im.pixel_array.astype(float)

    rescaled_image = (np.maximum(im, 0)/im.max())*255 #pixels' float
    final_image = np.uint8(rescaled_image) #int pixels
    final_image = Image.fromarray(final_image)
    return final_image

names = get_names('MassTest')
for name in names:
    image = convert_dcm_png('MassTest/'+name)
    name = name.rsplit(".", 2)[0]
    image.save("PNGOutput/"+ name + '.png')

    
