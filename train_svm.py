import os
from os import listdir
from os.path import isfile, join
import glob
import pickle
import time
from scipy.misc import imread
from sklearn.svm import LinearSVC
from scipy.misc import imread,imsave,imresize

import numpy as np
import os
import itertools
import operator
import random
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from skimage.feature import hog
from skimage import color, exposure
from scipy.misc import imread,imsave,imresize
import numpy.random as nprnd
from sklearn.svm import SVC
from sklearn import linear_model
from sklearn.svm import LinearSVC
import matplotlib
import pickle


good =  glob.glob("2ndacc/good/*")
bad = glob.glob("2ndacc/bad/*")

print good
data = []
labels = []
good_data = []
good_labels = []

for i in good:
    image = imread(i, 1)
    image = imresize(image, (200, 200))
    hog_feat = hog(image, orientations=12, pixels_per_cell=(16,16), cells_per_block=(1,1))
    data.append(hog_feat)
    #good_data.append(image.ravel())
    #good_labels.append
    labels.append(0)

for i in bad:
    image = imread(i, 1)
    image = imresize(image, (200, 200))
    hog_feat = hog(image, orientations=12, pixels_per_cell=(16,16), cells_per_block=(1,1))
    data.append(hog_feat)
    #good_data.append(image.ravel())
    #good_labels.append
    labels.append(1)

print ' training svm'
clf = LinearSVC(dual=False, verbose=1)
clf.fit(data, labels)
pickle.dump(clf, open("svm.detector", "wb"))