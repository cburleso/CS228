import sys
sys.path.insert(0, '..')
from pygameWindow import PYGAME_WINDOW
from pygameWindow_Del03 import PYGAME_WINDOW
import Leap
import constants
import numpy as np

class DELIVERABLE:
    def __init__(self):
        self.controller = Leap.Controller()
        self.pygameWindow = PYGAME_WINDOW()
        self.x = 400
        self.y = 400
        self.xMin = 1000.0
        self.xMax = -1000.0
        self.yMin = 1000.0
        self.yMax = -1000.0
        self.previousNumberOfHands = 0
        self.currentNumberOfHands = 0
        self.gestureData = np.zeros((5, 4, 6), dtype='f')

    def Handle_Frame(self, frame):
        global x, y, xMin, xMax, yMin, yMax
        hand = frame.hands[0]
        fingers = hand.fingers
        i = 0
        for finger in fingers:
            self.Handle_Finger(finger, i)
            i += 1

        if self.Recording_Is_Ending():
            print(self.gestureData)
    
    def Handle_Finger(self, finger, i):
        for j in range(4):
            bone = finger.bone(j)
            fingerWidth = 4 - j
            self.Handle_Bone(bone, fingerWidth, i, j)

    def Handle_Bone(self, bone, fingerWidth, i, j):
        
        tip = bone.next_joint
        base = bone.prev_joint
        
        # For gesture recording
        if self.Recording_Is_Ending():
            self.gestureData[i,j,0] = base[0]
            self.gestureData[i,j,1] = base[1]
            self.gestureData[i,j,2] = base[2]
            
            self.gestureData[i,j,3] = tip[0]
            self.gestureData[i,j,4] = tip[1]
            self.gestureData[i,j,5] = tip[2]
        
        xBase, yBase = self.Handle_Vector_From_Leap(base)
        xTip, yTip = self.Handle_Vector_From_Leap(tip)
        if self.currentNumberOfHands == 1:
            handColor = (102, 255, 102) # Green 
        else:
            handColor = (255, 0, 0) # Red
        self.pygameWindow.Draw_Line(xBase, yBase, xTip, yTip, fingerWidth, handColor)

    def Handle_Vector_From_Leap(self, v):
        global xMax, xMin, yMax, yMin
        xVal = v[0]
        yVal = v[1]
        # Scale 
        xVal = (constants.pygameWindowWidth / 300) * v[0] + .5 * constants.pygameWindowWidth
        yVal = (500 - v[1]) * constants.pygameWindowDepth / 400
        return xVal, yVal

    def Recording_Is_Ending(self):
        if (self.previousNumberOfHands == 2):
            if (self.currentNumberOfHands == 1):
                return True

    def Run_Forever(self):
        while True: # Run until the user shuts down the program
            self.Run_Once()
            

    def Run_Once(self):
        self.pygameWindow.Prepare() # Create user window
        frame = self.controller.frame() # Capture a frame object for hand detection
        self.currentNumberOfHands = len(frame.hands)
        if (len(frame.hands) > 0):
            self.Handle_Frame(frame)
        self.pygameWindow.Reveal() # Update window frame
        self.previousNumberOfHands = self.currentNumberOfHands
        
    
        
        
