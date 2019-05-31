# Rail_reactor_test_task

This is console program for comparing images in given directory. 

Usage: python solution.py [-h] --path PATH

optional arguments:
-h, --help            show this help message and exit
--path PATH           folder with images

Two algorithm are used - Mean Square Error(MSE) and Structure similar index(SSIM). 

Program is not perfect - sometimes it gives false positive or loses some values. 
On test images it loses 6 and 6_similar.
