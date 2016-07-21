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
names2 =        "http://images.gotinder.com/577040ea19c4986f1250320c/6d9498f1-7967-4912-9e7a-6d32be8150eb.jpg"
names3 =        "http://images.gotinder.com/57310df1d6290d1a1a7e5be8/d05a163a-1179-4bff-8a80-23633b0e3b2b.jpg"


#print names[27:51]
#print names2[27:51]
#print names3[27:51]

# good/bad
identifiers = ['G', 'B']

source = glob.glob("../2ndacc/testing/*")
print source;
counter = 0
for i in source:
    testing = imread(i, 1)
    testing = imresize(testing, (200, 200))
    hog_features = hog(testing, orientations=12, pixels_per_cell=(16, 16),
                       cells_per_block=(1, 1))
    result_type = identifiers[0]
    print i[18:-4]
    #Image.open(i).save('../2ndacc/AIResults/svmHOG/' + str(identifiers[result_type]) + i[18:-3] + ".jpg")

    counter += 1


