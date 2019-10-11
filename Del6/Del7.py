import sys
sys.path.insert(0, '../..') 
import Leap 
import constants
import pickle 
from pygameWindow import PYGAME_WINDOW 
import random
import numpy as np
import threading

##clf = pickle.load(open('userData/classifier.p', 'rb'))
##testData = np.zeros((1, 30), dtype = 'f')

controller = Leap.Controller()
pygameWindow = PYGAME_WINDOW() # Create user display window 
print(pygameWindow)

x = 400 
y = 400

xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0

programState = 0

def Handle_Frame(frame):
    global x, y, xMin, xMax, yMin, yMax
    hand = frame.hands[0]
    fingers = hand.fingers
    for finger in fingers:
        Handle_Finger(finger)


def Handle_Finger(finger):
    for i in range(4):
        bone = finger.bone(i)
        fingerWidth = 4 - i
        Handle_Bone(bone, fingerWidth)
        
def Handle_Bone(bone, fingerWidth):
    tip = bone.next_joint
    base = bone.prev_joint
    xBase, yBase = Handle_Vector_From_Leap(base)
    xTip, yTip = Handle_Vector_From_Leap(tip)
    pygameWindow.Draw_Black_Line(xBase, yBase, xTip, yTip, fingerWidth)
    
def Handle_Vector_From_Leap(v):
    global xMax, xMin, yMax, yMin
    xVal = v[0]
    yVal = v[2]

    if (xVal < xMin):
        xMin = xVal
    if (xVal > xMax):
        xMax = xVal
        
    if (yVal < yMin):
        yMin = yVal
    if (yVal > yMax):
        yMax = yVal
        
    # Scale x and y coordinates
    xVal = Scale(xVal, xMin, xMax, 0, constants.pygameWindowWidth)
    yVal = Scale(yVal, yMin, yMax, 0, constants.pygameWindowDepth) 

    return xVal, yVal

def Scale(val, minOldRange, maxOldRange, minNewRange, maxNewRange):
    maxNewRange = maxNewRange / 2
    diff = val - minOldRange
    oldRange = maxOldRange - minOldRange
    newRange = maxNewRange - minNewRange
    if (oldRange == 0):
        return val
    oldFraction = diff / oldRange
    newVal = oldFraction * newRange
    return newVal

def CenterData(X):
	allXCoordinates = X[0,::3]
	XmeanValue  = allXCoordinates.mean()
	X[0,::3] = allXCoordinates - XmeanValue

	allYCoordinates = X[0,1::3]
	YmeanValue  = allYCoordinates.mean()
	X[0,1::3] = allYCoordinates - YmeanValue

	allZCoordinates = X[0,2::3]
	ZmeanValue  = allZCoordinates.mean()
	X[0,2::3] = allZCoordinates - ZmeanValue

	return X

def DrawImageToHelpUserPutTheirHandOverTheDevice():
    pygameWindow.Prepare()
    pygameWindow.drawHandImage()
    pygameWindow.Reveal()

def promptMoveLeft():
    pygameWindow.promptHandLeft()
    pygameWindow.Reveal()

def promptMoveRight():
    pygameWindow.promptHandRight()
    pygameWindow.Reveal()

def promptMoveUp():
    pygameWindow.promptHandUp()
    pygameWindow.Reveal()

def promptMoveDown():
    pygameWindow.promptHandDown()
    pygameWindow.Reveal()

def promptCenterSuccess():
    pygameWindow.promptGreenCheck()
    pygameWindow.Reveal()
    
    
def HandOverDevice():
    frame = controller.frame()
    if (len(frame.hands) > 0):
        return True
    else:
        return False
    
def HandleState0():
    global programState
    DrawImageToHelpUserPutTheirHandOverTheDevice()
    if HandOverDevice():
        programState = 1
    
    
def HandleState1():
    global programState
    pygameWindow.Prepare() 
    frame = controller.frame() 
    if HandOverDevice():
        hand = frame.hands[0]
        Handle_Frame(frame)
        
        #--------Hand Centering - Using Base of Middle Metacarpal ---------#
        
        fingers = hand.fingers
        targetFinger = fingers[2]
        targetBone = targetFinger.bone(0) # Middle Metacarpal
        targetJoint = targetBone.prev_joint
        xBaseJoint, yBaseJoint = Handle_Vector_From_Leap(targetJoint) # X and Y coordinate of target joint
        print(xBaseJoint)
        print(yBaseJoint)
        print()
        if (xBaseJoint <= 110):
            promptMoveRight()
        if (xBaseJoint >= 225):
            promptMoveLeft()
        if (yBaseJoint <= 250):
            promptMoveDown()
        if (yBaseJoint >= 350):
            promptMoveUp()
        if (xBaseJoint > 110):
            if (xBaseJoint < 225):
                if (yBaseJoint > 250):
                    if (yBaseJoint < 350):
                        promptCenterSuccess()
                        
                
        
    pygameWindow.Reveal()
    if HandOverDevice() == False:
        programState = 0
    
    

while True:
    if programState == 0:
        HandleState0()
    elif programState == 1:
        HandleState1()
    
    
##        k = 0
##        for finger in range(5):
##            finger = hand.fingers[finger]
##            for b in range(4):
##                if b == 0:
##                    bone = finger.bone(Leap.Bone.TYPE_METACARPAL)
##                elif b == 1:
##                    bone = finger.bone(Leap.Bone.TYPE_PROXIMAL)
##                elif b == 2:
##                    bone = finger.bone(Leap.Bone.TYPE_INTERMEDIATE)
##                elif b == 3:
##                    bone = finger.bone(Leap.Bone.TYPE_DISTAL)
##
##                boneBase = bone.prev_joint
##                boneTip = bone.next_joint
##
##                xBase = boneBase[0]
##                yBase = boneBase[1]
##                zBase = boneBase[2]
##                xTip  = boneTip[0]
##                yTip  = boneTip[1]
##                zTip  = boneTip[2]
##                
##                if ((b == 0)or(b == 3)):
##                    testData[0, k] = xTip
##                    testData[0, k+1] = yTip
##                    testData[0, k+2] = zTip
##                    k = k+3
##        #print(testData)
##        testData = CenterData(testData)
##        predictedClass = clf.Predict(testData)
##        print(predictedClass)
##   
 


