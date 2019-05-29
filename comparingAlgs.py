import numpy as np
from PIL import Image as PILImage

def rgbToGray(r, g, b):
    return (0.3 * r) + (0.59 * g) + (0.11 * b)

def pixelToGray(pixel):
    return rgbToGray(pixel[0], pixel[1], pixel[2])

def mse(imageA, imageB, step = 1):
    imageB = imageB.resize(imageA.size)

    pixelsA = imageA.getdata()
    pixelsB = imageB.getdata()

    size = len(pixelsA)

    grayA = [0] * size
    grayB = [0] * size

    for i in range(0, size, step):
        grayA[i] = pixelToGray(pixelsA[i])
        grayB[i] = pixelToGray(pixelsB[i])

    err = 0
    for i in range(0, size, step):
        err += (grayA[i] - grayB[i]) ** 2

    err /= size

    return err


# def ssim(img1, img2, cs_map=False):
#     img1 = img1.astype(numpy.float64)
#     img2 = img2.astype(numpy.float64)
#     size = 11
#     sigma = 1.5
#     window = gauss.fspecial_gauss(size, sigma)
#     K1 = 0.01
#     K2 = 0.03
#     L = 255 #bitdepth of image
#     C1 = (K1*L)**2
#     C2 = (K2*L)**2
#     mu1 = signal.fftconvolve(window, img1, mode='valid')
#     mu2 = signal.fftconvolve(window, img2, mode='valid')
#     mu1_sq = mu1*mu1
#     mu2_sq = mu2*mu2
#     mu1_mu2 = mu1*mu2
#     sigma1_sq = signal.fftconvolve(window, img1*img1, mode='valid') - mu1_sq
#     sigma2_sq = signal.fftconvolve(window, img2*img2, mode='valid') - mu2_sq
#     sigma12 = signal.fftconvolve(window, img1*img2, mode='valid') - mu1_mu2
#     if cs_map:
#         return (((2*mu1_mu2 + C1)*(2*sigma12 + C2))/((mu1_sq + mu2_sq + C1)*
#                     (sigma1_sq + sigma2_sq + C2)),
#                 (2.0*sigma12 + C2)/(sigma1_sq + sigma2_sq + C2))
#     else:
#         return ((2*mu1_mu2 + C1)*(2*sigma12 + C2))/((mu1_sq + mu2_sq + C1)*
#                     (sigma1_sq + sigma2_sq + C2))


