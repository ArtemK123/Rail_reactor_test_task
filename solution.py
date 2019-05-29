import os, sys
import numpy as np
import itertools
import multiprocessing as mp
import time
import math
import comparingAlgs as algs
from PIL import Image as PILImage

helpText = '''
usage: solution.py [-h] --path PATH

First test task on images similarity.

optional arguments:
-h, --help            show this help message and exit
--path PATH           folder with images
'''

withoutPathText = '''
solution.py: error: the following arguments are required: --path
'''

wrongDirText = '''
solution.py: error: given directory doesn`t exist
'''

class Image:
    def __init__(self, path):
        self.path = path
        self.object = PILImage.open(path)

    object = None
    path = ''

images = dict()

def findSimilar(dirpath):
    filePathes = [os.path.join(dirpath, f) for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]

    images = []
    for path in filePathes:
        images.append(Image(path))

    imagePairs = itertools.combinations(images, 2)

    searchStart = time.process_time()
    for pair in imagePairs:
        step = int(min(pair[0].object.size[0] * pair[0].object.size[1], pair[1].object.size[0] * pair[1].object.size[1]) / 10000)
        start = time.process_time()
        res = algs.mse(pair[0].object, pair[1].object, step)

        print("-----------")
        print(pair[0].path, pair[1].path)
        print('Time - ', time.process_time() - start, 'MSE - ', res)

        if (res < 4000.0):
            print("\nSimilar images found !!!\n")
    print('Search has taken - ', time.process_time() - searchStart)

# console working module
if (len(sys.argv) == 3):
    if (sys.argv[1] == '--path'):
        if os.path.isdir(sys.argv[2]):
            findSimilar(sys.argv[2])
        else:
            print(wrongDirText)
    else:
        print(withoutPathText)
elif (len(sys.argv) == 2):
    if (sys.argv[1] == '-h' or sys.argv[1] == '--help'):
        print(helpText)
    elif (sys.argv[1] == '--path'):
        print(wrongDirText)
    else:
        print(withoutPathText)

# pool = mp.Pool(mp.cpu_count())
# results = [pool.apply(checkSimilarImages, args=(pair)) for pair in filePairs]


# im1 = PILImage.open('./dev_dataset/dev_dataset/11.jpg')
# im2 = PILImage.open('./dev_dataset/dev_dataset/11_duplicate.jpg')
#
# startTime = time.process_time()
# print("MSE result - ", algs.mse(im1, im2, 10))
# print("Time of work - ", time.process_time() - startTime)
