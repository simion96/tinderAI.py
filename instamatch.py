from random import uniform
from math import fabs
print ("hey")
currentLoc = [51.065812, -0.335402]
lowerLimit = 0.005
idealLimit = 0.05
upperLimit = 0.075
#0.000100, 0.000100 diff - couple of houses away
#51.065000, -0.335000, 51.065999, -0.335999 100m
#51.060000, -0.330000, 51.069999, -0.339999 3.15km
#51.030000, -0.300000, 51.039999, -0.399999 7.9km


#while true:
#dps = []
#for i, c in enumerate(currentLoc):
#    dps.append(c.split(".")[1])
    #065812, 335402
#while dps[0] > 
while True:
    newLoc = []
    if (random.choice([True, False]) == True):
        newLoc = [uniform(currentLoc[0], currentLoc[0]+upperLimit), uniform(currentLoc[1], currentLoc[1]+upperLimit)]
    else:
        newLoc = [uniform(currentLoc[0], currentLoc[0]-upperLimit), uniform(currentLoc[1], currentLoc[1]-upperLimit)]
    #print ( str(newLoc[0]) + " " + str(newLoc[1]))
    
    if (fabs(newLoc[0] - currentLoc[0]) > lowerLimit) and (fabs(newLoc[1] - currentLoc[1]) < upperLimit):
        print ("{} {}".format(newLoc[0], newLoc[1]))
#curLocDec = float(currentLoc[0])
#print(str(curLocDec[0]))
