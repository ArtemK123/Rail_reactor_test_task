import os, sys
import numpy as np
import itertools
import multiprocessing as mp
from PIL import Image

im1 = Image.open('./dev_dataset/dev_dataset/1.jpg')
im2 = Image.open('./dev_dataset/dev_dataset/1_duplicate.jpg')

def rgbToGray(r, g, b):
    return (0.3 * r) + (0.59 * g) + (0.11 * b)

def pixelToGray(pixel):
    return rgbToGray(pixel[0], pixel[1], pixel[2])


def mse(imageA, imageB):
    imageB = imageB.resize(imageA.size)

    pixelsA = np.asanyarray(imageA.getdata())
    pixelsB = np.asanyarray(imageB.getdata())

    err = (np.square(map(lambda pixel: pixelToGray, pixelsA) - map(lambda pixel: pixelToGray, pixelsB))).mean(2)

    return err

def checkSimilarImages(pathPairs):
    result = []
    for pair in pathPairs:
        image1 = images[pair[0]]
        image2 = images[pair[1]]
        if (mse(image1, image2) == 0):
            result.append(pair)

dirpath = sys.argv[1]
filePathes = [os.path.join(dirpath, f) for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]

images = dict()
for path in filePathes:
    images[path] = Image.open(path)

filePairs = itertools.combinations(filePathes, 2)

# pool = mp.Pool(mp.cpu_count())
# results = [pool.apply(checkSimilarImages, args=(pair)) for pair in filePairs]

print(mse(im1, im2))



# for pair in filePairs:
#     if (mse(images[pair[0]], images[pair[1]]) == 0):
#         print(pair)

#
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