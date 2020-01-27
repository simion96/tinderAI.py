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

good =  glob.glob("./../2ndacc/good/*")
bad = glob.glob("./../2ndacc/bad/*")

data = list()
labels = list()
good_data = []
good_labels = []

for i in range(len(good)):
    for filename in good[i]:
        image = imread(i, 1)
        imr = image.ravel()
        data.append(imr)
        labels.append(0)

for i in range(len(bad)):
    for filename in bad[i]:
        image = imread(i, 1)
        imr = image.ravel()
        data.append(imr)
        labels.append(1)

clf = LinearSVC(dual=False, verbose=1)
clf.fit(data, labels)
pickle.dump(clf, open("svmravel.detector", "wb"))
