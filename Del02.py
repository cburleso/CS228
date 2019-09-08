import sys
sys.path.insert(0, '..') # Used to allow program to find necessary packages
import Leap # Module used to interact with Leap Motion device
import constants

controller = Leap.Controller() # Create an instance of a controller object 
from pygameWindow import PYGAME_WINDOW # Import class containing visual program
# functions
import random


x = 400 # Initial x position for dot 
y = 400 # Initial y position for dot

timer = 0

# Boundaries for dot movement within window 
xMin = 1000.0
xMax = -1000.0
yMin = 1000.0
yMax = -1000.0

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
    yVal = v[3]

    # Scale x and y coordinates
    xVal = (constants.pygameWindowWidth / 300) * v[0] + .5 * constants.pygameWindowWidth
    yVal = (500 - v[1]) * constants.pygameWindowDepth / 400 

    return xVal, yVal
    
    
    
     
# Initialize an instance of the PYGAME_WINDOW class to create function calls      
pygameWindow = PYGAME_WINDOW()
print(pygameWindow)

while True: # Run until the user shuts down the program
    pygameWindow.Prepare() # Create user window
   
    frame = controller.frame() # Create a frame object for hand detection
    
    if (len(frame.hands) > 0):
        Handle_Frame(frame)
   
    pygameWindow.Reveal() # Update window frame 


