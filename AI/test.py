import numpy as np
from skimage.feature import hog
from scipy.misc import imread,imresize,imsave
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
import matplotlib.pyplot as plt
import glob
import pickle
from PIL import Image
import scipy.misc
import warnings

warnings.filterwarnings(action="ignore", category=DeprecationWarning)
names = "http://images.gotinder.com/55f5f20482f96dff09d79380/7bfbe387-55e0-46bb-ab35-cef3ca3a6536.jpg"
#print names[27:51]

# good/bad
identifiers = ['G', 'B']

source = glob.glob("../2ndacc/testing/*")
counter = 0
for i in source:
    testing = imread(i, 1)
    testing = imresize(testing, (200, 200))
    hog_features = hog(testing, orientations=12, pixels_per_cell=(16, 16),
                       cells_per_block=(1, 1))
    result_type = identifiers[0]
    print i[18:-4]
    counter += 1


