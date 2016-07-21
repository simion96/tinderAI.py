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

if __name__ == '__main__':
    #load the detector
    clf = pickle.load( open("svmhog.detector","rb"))

    identifiers = ['good', 'bad']

    source = glob.glob("../2ndacc/testing/*")
    print source;
    counter = 0
    for i in source:
        testing = imread(i, 1)
        testing = imresize(testing, (200, 200))
        hog_features = hog(testing, orientations=12, pixels_per_cell=(16, 16),
                           cells_per_block=(1, 1))
        result_type = clf.predict(hog_features)
        Image.open(i).save('../2ndacc/AIResults/svmHOG/' + str(identifiers[result_type])+ str(counter)+".jpg")
        counter +=1


