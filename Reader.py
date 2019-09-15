import pickle
import os
import constants
from pygameWindow_Del03 import PYGAME_WINDOW
class READER:
    def __init__(self):
        self.numGestures = 0
        self.Count_Gestures()
        self.pygameWindow = PYGAME_WINDOW()
        
    def Count_Gestures(self):
        path, dirs, files = next(os.walk('userData'))
        self.numGestures = len(files)

    def Print_Gestures(self):
        for i in range(self.numGestures):
            pickleIn = open('C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/userData/gesture%s.p' % i, 'rb')
            gestureData = pickle.load(pickleIn)
            print(gestureData)

    def Draw_Gestures(self):
        while True:
            self.Draw_Each_Gesture_Once()
            

    def Draw_Each_Gesture_Once(self):
        for i in range(self.numGestures):
            self.Draw_Gesture(i)

    def Scale_Coordinates(self, x, y):
        xVal = (constants.pygameWindowWidth / 300) * x + .5 * constants.pygameWindowWidth
        yVal = (500 - y) * constants.pygameWindowDepth / 400
        return xVal, yVal 
        

    def Draw_Gesture(self, i):
        self.pygameWindow.Prepare()
        pickleIn = open('C:/Users/CHBADMIN/Desktop/LeapDeveloperKit_2.3.1+31549_win/LeapSDK/lib/x86/CS228/userData/gesture%s.p' % i, 'rb')
        gestureData = pickle.load(pickleIn)
        print(gestureData)
        
        for i in range(5):
            for j in range(4):
                # base 
                xBaseNotYetScaled = gestureData[i,j,0] 
                yBaseNotYetScaled = gestureData[i,j,1] 
                 
                # tip 
                xTipNotYetScaled = gestureData[i,j,3] 
                yTipNotYetScaled = gestureData[i,j,4]

                xBase, yBase = self.Scale_Coordinates(xBaseNotYetScaled, yBaseNotYetScaled)
                xTip, yTip = self.Scale_Coordinates(xTipNotYetScaled, yTipNotYetScaled)

                self.pygameWindow.Draw_Line(xBase, yBase, xTip, yTip, 1, (0, 0, 255)) 
                
 
        self.pygameWindow.Reveal()
        
        
            
