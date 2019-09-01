import sys
sys.path.insert(0, '..')
import Leap

controller = Leap.Controller()
##from pygameWindow import PYGAME_WINDOW
##import random
##x = 400
##y = 400
##
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
##        
##pygameWindow = PYGAME_WINDOW()
##
##print(pygameWindow)
while True:
    frame = controller.frame()
    if (len(frame.hands) > 0):
        print "hand detected."
##    pygameWindow.Prepare()
##    pygameWindow.Draw_Black_Circle(x, y)
##    Perturb_Circle_Position()
##    pygameWindow.Reveal()


