import numpy as np
from PIL import Image as PILImage

def rgbToGray(r, g, b):
    return (0.3 * r) + (0.59 * g) + (0.11 * b)

def pixelToGray(pixel):
    return rgbToGray(pixel[0], pixel[1], pixel[2])

def mseNumpy(imageA, imageB, *args):
    if (imageA.size[0] * imageA.size[1] > imageB.size[0] * imageB.size[1]):
        imageA = imageA.resize(imageB.size)
    else:
        imageB = imageB.resize(imageA.size)

    pixelsA = np.array(imageA.convert("L"))
    pixelsB = np.array(imageB.convert("L"))

    err = np.square(pixelsA - pixelsB).mean()
    return err



def mse(imageA, imageB, step = 1):
    if (imageA.size[0] * imageA.size[1] > imageB.size[0] * imageB.size[1]):
        imageA = imageA.resize(imageB.size)
    else:
        imageB = imageB.resize(imageA.size)

    pixelsA = imageA.convert("L").getdata()
    pixelsB = imageB.convert("L").getdata()

    err = 0
    for i in range(0, len(pixelsA), step):
        err += (pixelsA[i] - pixelsB[i]) ** 2

    err /= (len(pixelsA) / step)

    return err


