import numpy as np
from skimage.feature import hog
from scipy.misc import imread,imresize
from sklearn.svm import SVC
from sklearn.svm import LinearSVC
import pickle

if __name__ == '__main__':
    #load the detector
    clf = pickle.load( open("svm.detector","rb"))

    #now load a test image and get the hog features.
    test_image = imread('2ndacc/testing/105',1)
    test_image = imresize(test_image, (200,200))

    hog_features = hog(test_image, orientations=12, pixels_per_cell=(16, 16),
                    cells_per_block=(1, 1))
    identifiers = ['good', 'bad']
    result_type = clf.predict(hog_features)
    print "the image provided is: " + identifiers[result_type]


