import sys
sys.path.insert(0, '../..') 
import Leap 
import constants
import pickle 
from pygameWindow import PYGAME_WINDOW 
import random
import numpy as np
import threading
import time 

# User login 
database = pickle.load(open('userData/database.p', 'rb'))

userName = raw_input('Please enter your name: ')

if userName in database:
    print('Welcome back, ' + userName + '.')
    database[userName]['logins'] += 1

else:
    database[userName] = {'logins' : 1}
    print('Welcome, ' + userName + '.')

print(database)
pickle.dump(database, open('userData/database.p', 'wb'))

    
clf = pickle.load(open('userData/classifier.p', 'rb'))
testData = np.zeros((1, 30), dtype = 'f')

controller = Leap.Controller()
pygameWindow = PYGAME_WINDOW() # Create user display window 
print(pygameWindow)

x = 400 
y = 400

xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0

handCenteredTimer = 0
greenCheckTimer = 0
randDigitTimer = 0
signCorrect = 0

numIndex = 0
levelOneNums = [0, 1, 2, 3]
#digitToSign = random.randrange(0, 9) # Initial digit to sign
digitToSign = levelOneNums[numIndex]




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

def HandCentered():
    frame = controller.frame() 
    centered = True
    hand = frame.hands[0]
    fingers = hand.fingers
    targetFinger = fingers[2]
    targetBone = targetFinger.bone(0) 
    targetJoint = targetBone.prev_joint
    xBaseJoint, yBaseJoint = Handle_Vector_From_Leap(targetJoint)
    if (xBaseJoint <= 110):
        centered = False
    if (xBaseJoint >= 225):
        centered = False
    if (yBaseJoint <= 250):
        centered = False
    if (yBaseJoint >= 350):
        centered = False
    return centered

def DrawImageToHelpUserPutTheirHandOverTheDevice():
    pygameWindow.Prepare()
    pygameWindow.drawHandImage()
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
    global programState, handCenteredTimer
    pygameWindow.Prepare() 
    frame = controller.frame() 
    if (handCenteredTimer > 100):
            programState = 2
    hand = frame.hands[0]
    Handle_Frame(frame)
        
    fingers = hand.fingers
    targetFinger = fingers[2]
    targetBone = targetFinger.bone(0) # Middle Metacarpal
    targetJoint = targetBone.prev_joint
    xBaseJoint, yBaseJoint = Handle_Vector_From_Leap(targetJoint) 

    if (xBaseJoint <= 110):
        pygameWindow.promptHandRight()
        handCenteredTimer = 0
    if (xBaseJoint >= 225):
        pygameWindow.promptHandLeft()
        handCenteredTimer = 0
    if (yBaseJoint <= 250):
        pygameWindow.promptHandDown()
        handCenteredTimer = 0
    if (yBaseJoint >= 350):
        pygameWindow.promptHandUp()
        handCenteredTimer = 0
    if (xBaseJoint > 110): # If hand is centered 
        if (xBaseJoint < 225):
            if (yBaseJoint > 250):
                if (yBaseJoint < 350):
                    pygameWindow.promptThumbsUp()
                    handCenteredTimer += 1
                                            
    if HandOverDevice() == False:
        programState = 0
        handCenteredTimer = 0

    pygameWindow.Reveal()
    
    
def HandleState2():
    global programState, digitToSign, testData, clf, signCorrect, randDigitTimer, handCenteredTimer, levelOneNums, numIndex
    randDigitTimer += 1 # Time viewing random digit 
    database = pickle.load(open('userData/database.p', 'rb'))
    pygameWindow.Prepare() 
    if HandOverDevice(): 
        frame = controller.frame() 
        hand = frame.hands[0]
        Handle_Frame(frame)
        if (HandCentered() == False):
            handCenteredTimer = 0
            programState = 1
            
        pygameWindow.promptASLnum(digitToSign)
        pygameWindow.promptASLsign(digitToSign)

        # Get number of times user has been presented with digit
        userRecord = database[userName]
        attemptsDict = 'digit' + str(digitToSign) + 'attempts'
        try:
            numSeen = database[userName][attemptsDict]
        except:
            userRecord[attemptsDict] = 1
            numSeen = 1
                    
        pygameWindow.promptNumSeen(numSeen)

        # KNN
        k = 0
        for finger in range(5):
            finger = hand.fingers[finger]
            for b in range(4):
                if b == 0:
                    bone = finger.bone(Leap.Bone.TYPE_METACARPAL)
                elif b == 1:
                    bone = finger.bone(Leap.Bone.TYPE_PROXIMAL)
                elif b == 2:
                    bone = finger.bone(Leap.Bone.TYPE_INTERMEDIATE)
                elif b == 3:
                    bone = finger.bone(Leap.Bone.TYPE_DISTAL)

                boneBase = bone.prev_joint
                boneTip = bone.next_joint

                xBase = boneBase[0]
                yBase = boneBase[1]
                zBase = boneBase[2]
                xTip  = boneTip[0]
                yTip  = boneTip[1]
                zTip  = boneTip[2]
                
                if ((b == 0)or(b == 3)):
                    testData[0, k] = xTip
                    testData[0, k+1] = yTip
                    testData[0, k+2] = zTip
                    k = k+3
        testData = CenterData(testData)
        predictedClass = clf.Predict(testData)
        print(predictedClass)
        
        if (predictedClass == digitToSign):
            signCorrect += 1
        else:
            signCorrect = 0

        if (randDigitTimer > 25): # Change digit and increment attempt if not signed correctly
            database[userName][attemptsDict] += 1 # Increment user attempt at digit 
            pickle.dump(database, open('userData/database.p', 'wb'))
            #digitToSign = random.randrange(0, 9)

            if (numIndex == 3):
                numIndex = 0
            else:
                numIndex += 1
                
            digitToSign = levelOneNums[numIndex]
            
            randDigitTimer = 0
            
            
        if (signCorrect == 10): # User successfully signed digit (recognized by KNN 10 times)
            successesDict = 'digit' + str(digitToSign) + 'successes'
            try:
                database[userName][successesDict] += 1
            except:
                userRecord[successesDict] = 1
                
            database[userName][attemptsDict] += 1 # Increment user attempt at digit
            pickle.dump(database, open('userData/database.p', 'wb'))
            randDigitTimer = 0
            
            if (numIndex == 3):
                numIndex = 0
            else:
                numIndex += 1
                    
            digitToSign = levelOneNums[numIndex]
            
            programState = 3
            
    else:
        programState = 0
        
    pygameWindow.Reveal()

def HandleState3(): # User 
    global programState, randNum, greenCheckTimer, numIndex, levelOneNums
    greenCheckTimer += 1
    pygameWindow.Prepare()
    frame = controller.frame()
    Handle_Frame(frame)
    pygameWindow.promptGreenCheck()
    if HandOverDevice():
        if HandCentered():
            if (greenCheckTimer > 100):
                #digitToSign = random.randrange(0, 9)
                
                programState = 2
                
                greenCheckTimer = 0
        else:
            programState = 1
            greenCheckTimer = 0
    else:
        programState = 0
        greenCheckTimer = 0
    pygameWindow.Reveal()

# Main program loop 
while True:
    if programState == 0:
        HandleState0()
    elif programState == 1:
        HandleState1()
    elif programState == 2:
        HandleState2()
    elif programState == 3:
        HandleState3()
    
    

   
 


