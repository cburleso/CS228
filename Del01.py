import sys
sys.path.insert(0, '..') # Used to allow program to find necessary packages
import Leap # Module used to interact with Leap Motion device
import constants

controller = Leap.Controller() # Create an instance of a controller object 
from pygameWindow import PYGAME_WINDOW # Import class containing visual program
# functions
import random # Random module used to generate random (x,y) coordinates for the
# black dot
x = 400 # Initial x position for dot 
y = 400 # Initial y position for dot

# Boundaries for dot movement within window 
xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0

# This function will randomly "roll" a four sided die, generating a random
# change in the x or y coordinate position of the dot within the window
##def Perturb_Circle_Position():
##    global x, y
##    fourSidedDieRoll = random.randint(1,4)
##    if fourSidedDieRoll == 1:
##        x -= 1
##    elif fourSidedDieRoll == 2:
##        x += 1
##    elif fourSidedDieRoll == 3:
##        y -= 1
##    else:
##        y += 1

def Handle_Frame(frame):
    global x, y, xMin, xMax, yMin, yMax
    hand = frame.hands[0]
    fingers = hand.fingers
    indexFingerList = fingers.finger_type(Leap.Finger.TYPE_INDEX)
    indexFinger = indexFingerList[0]
    distalPhalanx = indexFinger.bone(Leap.Bone.TYPE_DISTAL)
    tip = distalPhalanx.next_joint
    x = int(tip[0])
    y = int(tip[1])
    if (x < xMin):
        xMin = x
    if (x > xMax):
        xMax = x
    if (y < yMin):
        yMin = y
    if (y > yMax):
        yMax = y
    
def Scale(val, minVal, maxVal, lowVal, upVal):
    rangeOne = maxVal - minVal
    rangeTwo = upVal - lowVal
    if (val in range(int(minVal), int(maxVal))):
        val = abs(val)*3
    return val
    
     
# Initialize an instance of the PYGAME_WINDOW class to create function calls      
pygameWindow = PYGAME_WINDOW()
print(pygameWindow)

while True: # Run until the user shuts down the program
    pygameWindow.Prepare() # Creates user window
    
    frame = controller.frame() # Create a frame object for hand detection
    
    if (len(frame.hands) > 0):
        Handle_Frame(frame)

    pygameX = Scale(x, xMin, xMax, 0, constants.pygameWindowWidth)
    pygameY = Scale(y, yMin, yMax, 0, constants.pygameWindowDepth)
    
    pygameWindow.Draw_Black_Circle(int(pygameX), int(pygameY)) # Draw the black dot to the screen
    #Perturb_Circle_Position() # Randomly change dot position 
    pygameWindow.Reveal() # Update window frame 


