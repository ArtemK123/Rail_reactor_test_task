import os, sys
import numpy as np
import itertools
import time
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
    # this class represents image and it was creating for chaining path to image with pillow object
    def __init__(self, path):
        self.path = path
        self.object = PILImage.open(path)

    object = None
    path = ''

images = dict()

def findSimilar(dirpath):
    # finding all images in directory
    filePathes = [(dirpath + "/" + f) for f in os.listdir(dirpath) if os.path.isfile(os.path.join(dirpath, f))]

    images = []
    for path in filePathes:
        images.append(Image(path))

    imagePairs = itertools.combinations(images, 2)

    searchStart = time.process_time()
    for pair in imagePairs:
        step = int(min(pair[0].object.size[0] * pair[0].object.size[1], pair[1].object.size[0] * pair[1].object.size[1]) / 10000)
        start = time.process_time()

        mse = algs.mse(pair[0].object, pair[1].object, step)
        ssim = algs.mssim(pair[0].object.resize((512, 512)), pair[1].object.resize((512, 512)))

        # print("-----------")
        # print(pair[0].path, pair[1].path)
        # print('Time - ', time.process_time() - start, 'MSE - ', mse, 'SSIM - ', ssim)

        if (mse < 4000.0 and ssim > 0.4):
            print("-----------")
            print(pair[0].path.split('/').pop(), pair[1].path.split('/').pop())
            print('Time - ', time.process_time() - start, 'MSE - ', mse, 'SSIM - ', ssim)

    print('Search has taken - ', time.process_time() - searchStart)

# console working module
if (len(sys.argv) == 4 and (sys.argv[1] == '-h' or sys.argv[1] == '--help')):
    print(helpText)
elif (len(sys.argv) == 3):
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


