import numpy as np
from PIL import Image as PILImage

def rgbToGray(r, g, b):
    # function for transforming colored images to grayscale
    return (0.3 * r) + (0.59 * g) + (0.11 * b)

def pixelToGray(pixel):
    #
    return rgbToGray(pixel[0], pixel[1], pixel[2])

def makeSameSize(imageA, imageB):
    # this function make size of images equal to size of smaller picture

    if (imageA.size[0] * imageA.size[1] > imageB.size[0] * imageB.size[1]):
        imageA = imageA.resize(imageB.size)
    else:
        imageB = imageB.resize(imageA.size)
    return(imageA, imageB)

def mseNumpy(imageA, imageB, *args):
    # Mean Square Error for 2 images using numpy

    (imageA, imageB) = makeSameSize(imageA, imageB)

    pixelsA = np.array(imageA.convert("L"))
    pixelsB = np.array(imageB.convert("L"))

    err = np.square(pixelsA - pixelsB).mean()
    return err

def mse(imageA, imageB, step = 1):
    # Mean Square Error without numpy. If step != 1 - not every pixel will be used in comparing

    (imageA, imageB) = makeSameSize(imageA, imageB)

    pixelsA = imageA.convert("L").getdata()
    pixelsB = imageB.convert("L").getdata()

    err = 0
    for i in range(0, len(pixelsA), step):
        err += (pixelsA[i] - pixelsB[i]) ** 2

    err /= (len(pixelsA) / step)

    return err

def gaussFunction(x, y, sigma):
    # gauss function for 2d values
    return np.exp(-((x**2 + y**2)/(2*sigma**2))) / (2 * np.pi * sigma**2)

def gaussMatrix(width, height, sigma = 1.5):
    # function returns width*height Gauss matrix for weighting values
    # width and height must be odd


    stepX = int(width / 2)
    stepY = int(height / 2)
    matrix = np.zeros((width, height))
    for x in range(-stepX, stepX):
        for y in range(-stepY, stepY):
            matrix[x + stepX, y + stepY] = gaussFunction(x, y, sigma)
    return matrix

def ssim(A, B, weightMatrix = None):
    # ssim algorithm for grayscale image matrixs - was described by Zhou Wang
    # http://www.cns.nyu.edu/pub/lcv/wang03-preprint.pdf
    # A, B - matrixs of pixels, weightMatrix - gauss matrix, can be passed as argument or created in function

    if (A.shape != B.shape):
        raise Exception('matrixs have different size')

    if weightMatrix is None:
        weightMatrix = gaussMatrix(A.shape[0], A.shape[1])

    uA = (A * weightMatrix).sum()
    uB = (B * weightMatrix).sum()

    sigmaA = ((weightMatrix * np.square(A - uA)).sum())**(1/2)
    sigmaB = ((weightMatrix * np.square(B - uB)).sum())**(1/2)

    sigmaAB = (weightMatrix * (A - uA) * (B - uB)).sum()

    k1 = 0.01
    k2 = 0.03
    L = 2**8 - 1
    c1 = (k1*L)**2
    c2 = (k2*L)**2

    res = ((2*uA*uB + c1) * (2*sigmaAB + c2)) / ((uA**2 + uB**2 + c1) * (sigmaA**2 + sigmaB**2 + c2))
    return res

def mssim(imageA, imageB):
    # function returns mean structural similarity index for 2 images
    # there is used the 11x11 frame and it`s moved through images

    (imageA, imageB) = makeSameSize(imageA, imageB)
    winSize = 11

    pixelsA = np.array(imageA.convert('L'))
    pixelsB = np.array(imageB.convert('L'))

    weightMatrix = gaussMatrix(winSize, winSize)

    blocks = int(len(pixelsA) / winSize)

    ssimMatrix = np.zeros((blocks, blocks))
    for i in range(0, blocks):
        for j in range(0, blocks):
            ssimMatrix[i, j] = ssim(pixelsA[i*winSize:(i+1)*winSize, j*winSize:(j+1)*winSize], pixelsB[i*winSize:(i+1)*winSize, j*winSize:(j+1)*winSize], weightMatrix)

    return ssimMatrix.mean()




