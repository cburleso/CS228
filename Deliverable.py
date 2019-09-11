import sys
sys.path.insert(0, '..')
from pygameWindow import PYGAME_WINDOW
from pygameWindow_Del03 import PYGAME_WINDOW
import Leap
import constants

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

    def Handle_Frame(self, frame):
        global x, y, xMin, xMax, yMin, yMax
        hand = frame.hands[0]
        fingers = hand.fingers
        for finger in fingers:
            self.Handle_Finger(finger)

        if self.Recording_Is_Ending():
            print('recording is ending.')
    
    def Handle_Finger(self, finger):
        for i in range(4):
            bone = finger.bone(i)
            fingerWidth = 4 - i
            self.Handle_Bone(bone, fingerWidth)

    def Handle_Bone(self, bone, fingerWidth):
        tip = bone.next_joint
        base = bone.prev_joint
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
        yVal = v[3]

        # Scale x and y coordinates
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
        
    
        
        
