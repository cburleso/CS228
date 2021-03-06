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
import Tkinter as tk
from Tkinter import *
from PIL import Image, ImageTk

database = pickle.load(open('userData/database.p', 'rb'))
# Calculating top 3 users
mostCoins = 0
numUsers = 0
for name in database:
    numUsers += 1
    if (database[name]['numCoins'] > mostCoins):
        mostCoins = database[name]['numCoins']
        firstPlace = name + " (" + str(mostCoins) + ")"

# Calculate second place user
mostCoins2 = 0
for name in database:
    if ((database[name]['numCoins'] > mostCoins2) & (database[name]['numCoins'] < mostCoins)):
        mostCoins2 = database[name]['numCoins']
        secondPlace = name + " (" + str(mostCoins2) + ")"

# Calculate third place user
mostCoins3 = 0
for name in database:
    if ((database[name]['numCoins'] > mostCoins3) & (database[name]['numCoins'] < mostCoins2)):
        mostCoins3 = database[name]['numCoins']
        thirdPlace = name + " (" + str(mostCoins3) + ")"
        
if (numUsers == 0):
    firstPlace = "N/A"
    secondPlace = "N/A"
    thirdPlace = "N/A"


# -------------------TKINTER WINDOW START--------------------
userName = ""
root = tk.Tk()
canvas1 = tk.Canvas(root, width = 400, height = 300)
canvas1.pack()

entry1 = tk.Entry (root) 
canvas1.create_window(180, 220, window=entry1)

def getUsername():
    global userName, database
    userName = entry1.get()

    if userName in database:
        print('Welcome back, ' + userName + '.')
        database[userName]['logins'] += 1

    else:
        database[userName] = {'logins' : 1}
        userProgress = database[userName]
        userProgress['currDigitDict'] = [0, 1, 2]
        userProgress['numCoins'] = 0 
        print('Welcome, ' + userName + '.')

    print(database)
    pickle.dump(database, open('userData/database.p', 'wb'))
    root.destroy()

def showHighscores():
    load = Image.open("smallMedals.jpg")
    render = ImageTk.PhotoImage(load)
    img = Label(image=render)
    img.image = render
    img.place(x=-55, y=0) 
    text = Label(text=firstPlace)
    text.place(x=40, y=110)
    text2 = Label(text=secondPlace)
    text2.place(x=160, y=110)
    text3 = Label(text=thirdPlace)
    text3.place(x=296, y=110)
    
    
loginButton = tk.Button(text='Login', command=getUsername)
highscoreButton = tk.Button(text='Highscores', command=showHighscores)

canvas1.create_window(270, 220, window=loginButton)
canvas1.create_window(200, 260, window=highscoreButton)
root.mainloop()

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

prevNumCoins = database[userName]['numCoins'] # Get prev number of coins from user's last session 
handCenteredTimer = 0 # Timer for how long hand is centered before entering handleState1
greenCheckTimer = 0 # Timer for how long green check is presented to user 
digitTimer = 0 # Timer for how long user is presented with digit 
signCorrect = 0 # Number of times KNN recognizes digit successfully signed 
signTimer = 0 # Timer to maintain total duration of sign being presented 
numHearts = 3 # Number of "lives" user has (1 missed digit = 1 less life)
numCoins = 0 # Reset bag of coins to zero for each session 
numIndex = 0 # Index value which iterates over current digit dictionary for the user
coinStreak = 0
currDigitList = database[userName]['currDigitDict']
digitToSign = currDigitList[numIndex] # Initial digit to sign
globalCoinChange = 0
missTimer = 0
miss = False
programState = 0
beatPrev = 0


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
    global programState, digitToSign, testData, clf, signCorrect, digitTimer, handCenteredTimer, currDigitList, numIndex, signTimer, numCoins, prevNumCoins, numHearts, coinStreak, globalCoinChange, miss, missTimer, coinMiss, beatPrev
    digitTimer += 1 # Time viewing random digit
    signTimer += 1 # Time viewing ASL sign
    #database = pickle.load(open('userData/database.p', 'rb'))
    pygameWindow.Prepare() 
    if HandOverDevice():
        frame = controller.frame() 
        hand = frame.hands[0]
        Handle_Frame(frame)
        if (HandCentered() == False):
            handCenteredTimer = 0
            programState = 1
            
        attemptsDict = 'digit' + str(digitToSign) + 'attempts'
        successesDict = 'digit' + str(digitToSign) + 'successes'

        if (miss):
            if (missTimer < 5):
                missTimer += 1
                pygameWindow.promptMiss(coinMiss)
            else:
                miss = False
                missTimer = 0
                
            
        # Determine how much coins user earns for each success
        try:
            numSuccess = database[userName][successesDict]
        except:
            numSuccess = 0

        if (numSuccess == 0):
            coinChange = 1
        if (numSuccess == 1):
            coinChange = 1
        if (numSuccess == 2):
            coinChange = 2
        if (numSuccess > 2):
            coinChange = 3
        
        
        globalCoinChange = coinChange
        # Determine how long ASL gesture should be presented to user (depending on number of successes
        # with the current digit to sign) & length of time they have to sign the gesture 
        try:
            if (database[userName][successesDict] == 1):
                signTimerLimit = 25
                digitTimerLimit = 15
            elif (database[userName][successesDict] == 2):
                signTimerLimit = 10
                digitTimerLimit = 15
            elif (database[userName][successesDict] > 2):
                signTimerLimit = 0
                digitTimerLimit = 10 # Decrease time user has to sign digit
            elif (database[userName][successesDict] > 3):
                digitTimerLimit = 10
            else:
                signTimerLimit = 20 # Show ASL gesture the entire time
                digitTimerLimit = 15
        except:
            signTimerLimit = 25
            digitTimerLimit = 15
            
        if (signTimer < signTimerLimit):
            pygameWindow.promptASLsign(digitToSign)

        pygameWindow.promptASLnum(digitToSign)
        
        # Get number of times user has been presented with digit
        userRecord = database[userName]
        try:
            numSeen = database[userName][attemptsDict]
        except:
            userRecord[attemptsDict] = 1
            numSeen = 1
                    
        pygameWindow.promptNumSeen(numSeen)

        try:
            pygameWindow.promptNumSuccess(database[userName][successesDict])
        except:
            pygameWindow.promptNumSuccess(0)

        pygameWindow.promptCurrCoinBag(numCoins)

        pygameWindow.promptPrevCoins(prevNumCoins)

        pygameWindow.promptStreak(coinStreak)

        pygameWindow.promptClock(((digitTimer - digitTimerLimit) * -1))

        if (numHearts != 0):
            pygameWindow.promptNumHearts(numHearts)

        #pygameWindow.promptLeaderboard(firstPlace, secondPlace, thirdPlace)
        
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
        #print(predictedClass)
        
        if (predictedClass == digitToSign):
            pygameWindow.promptHoldHand()
            signCorrect += 1
        else:
            pygameWindow.promptIce()
            signCorrect = 0
            
        if (digitTimer > digitTimerLimit): # Change digit and increment attempt if not signed correctly
            coinMiss = coinChange
            miss = True
            database[userName][attemptsDict] += 1 # Increment user attempt at digit
            if (numCoins != 0):
                numCoins -= coinChange

            if (numHearts != 0):
                numHearts -= 1
                if (numHearts == 0):
                    numCoins = 0
                
            database[userName]['numCoins'] = numCoins
            pickle.dump(database, open('userData/database.p', 'wb'))
            # Change digit 
            if (numIndex == len(database[userName]['currDigitDict']) - 1):
                numIndex = 0
            else:
                numIndex += 1
                
            digitToSign = database[userName]['currDigitDict'][numIndex]
            digitTimer = 0
            coinStreak = 0 # Set coin streak back to zero 
            signTimer = 0
            
            
            
        if (signCorrect == 7): # User successfully signed digit (recognized by KNN 7 times)
            try:
                database[userName][successesDict] += 1
            except:
                userRecord[successesDict] = 1
                
            database[userName][attemptsDict] += 1 # Increment user attempt at digit
            digitTimer = 0
            
            coinStreak += 1 # Increment coin streak 
            if (coinStreak == 5):
                numCoins += 5
            elif (coinStreak == 10):
                numCoins += 15
            else:
                numCoins += coinChange # Increment number of gold coins depending on user success with digit (calculated for coinChange)

            if (prevNumCoins > 2):
                if (numCoins > prevNumCoins):
                    beatPrev += 1
                    if (beatPrev == 1):
                        numCoins += 10
            
            database[userName]['numCoins'] = numCoins # Update database info

            # Check if user passed 'level one' (digits 0 through 2)
            levelOnePass = True
            for digit in range(3):
                try:
                    digitDict = 'digit' + str(digit) + 'successes'
                    if (database[userName][digitDict] < 1):
                        levelOnePass = False
                        break
                except:
                    levelOnePass = False
                    break
                
            if (levelOnePass): # Change subset of digits shown to three new (3 through 5)
                database[userName]['currDigitDict'] = [0, 1, 2, 3, 4, 5]

            # Check if user passed 'level two' (digits 3 through 5)
            levelTwoPass = True
            for digit in range(3, 6):
                try:
                    digitDict = 'digit' + str(digit) + 'successes'
                    if (database[userName][digitDict] < 1):
                        levelTwoPass = False
                        break
                except:
                    levelTwoPass = False
                    break
                
            if (levelTwoPass): # Change subset of digits shown to four new (6 through 9) * all digits 
                database[userName]['currDigitDict'] = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

            # Increment to next digit in the list  
            if (numIndex == len(database[userName]['currDigitDict']) - 1):
                numIndex = 0
            else:
                numIndex += 1
            digitToSign = database[userName]['currDigitDict'][numIndex]
            pickle.dump(database, open('userData/database.p', 'wb'))
            signTimer = 0
            programState = 3
            

            
    else:
        programState = 0
        digitTimer = 0
        signTimer = 0
        
    pygameWindow.Reveal()

def HandleState3(): # To show 'success' check mark when user correctly signs digit 
    global programState, randNum, greenCheckTimer, numIndex, levelOneNums, numHearts, coinStreak, globalCoinChange, beatPrev
    if (coinStreak == 5):
        checkTimerLimit = 300
    elif (coinStreak == 10):
        checkTimerLimit = 300
    else:
        checkTimerLimit = 5
    if (beatPrev == 1):
        checkTimerLimit = 300
    greenCheckTimer += 1
    pygameWindow.Prepare()
    frame = controller.frame()
    Handle_Frame(frame)
    pygameWindow.promptSuccess(numHearts, coinStreak, globalCoinChange, beatPrev)
    if HandOverDevice():
        if HandCentered():
            if (greenCheckTimer > checkTimerLimit):
                if (numHearts != 3):
                    numHearts += 1
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
    
    

   
 


