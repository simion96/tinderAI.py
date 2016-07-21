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

    #good/bad
    identifiers = ['G', 'B']

    source = glob.glob("../2ndacc/testing/*")
    print source;
    counter = 0
    for i in source:
        testing = imread(i, 1)
        testing = imresize(testing, (200, 200))
        hog_features = hog(testing, orientations=12, pixels_per_cell=(16, 16),
                           cells_per_block=(1, 1))
        result_type = clf.predict(hog_features)
        #i[18:-4] - only id part of the filename
        Image.open(i).save('../2ndacc/AIResults/svmHOG/' + str(identifiers[result_type])+ i[18:-4] +".jpg")
        counter +=1

class Predictor(object):
    def __init__(self):
        print "initialized"

    @classmethod
    def predict(self, source):
        clf = pickle.load(open("AI/svmhog.detector", "rb"))

        # good/bad
        identifiers = ['G', 'B']

        print source;
        testing = imread(source, 1)
        testing = imresize(testing, (200, 200))
        hog_features = hog(testing, orientations=12, pixels_per_cell=(16, 16),
                           cells_per_block=(1, 1))
        result_type = clf.predict(hog_features)
        # i[18:-4] - only id part of the filename
        print "source in predictor is: " + source
        Image.open(source).save('2ndacc/AIResults/svmHOG1/' + str(identifiers[result_type]) + source[9:-4] + ".jpg")
        print source[9:-4]
        return str(identifiers[result_type])
