import sys
sys.path.insert(0, '..') # Used to allow program to find necessary packages
import Leap # Module used to interact with Leap Motion device 

controller = Leap.Controller() # Create an instance of a controller object 
from pygameWindow import PYGAME_WINDOW # Import class containing visual program
# functions
import random # Random module used to generate random (x,y) coordinates for the
# black dot
x = 400 # Initial x position for dot 
y = 400 # Initial y position for dot

# This function will randomly "roll" a four sided die, generating a random
# change in the x or y coordinate position of the dot within the window
def Perturb_Circle_Position():
    global x, y
    fourSidedDieRoll = random.randint(1,4)
    if fourSidedDieRoll == 1:
        x -= 1
    elif fourSidedDieRoll == 2:
        x += 1
    elif fourSidedDieRoll == 3:
        y -= 1
    else:
        y += 1

# Initialize an instance of the PYGAME_WINDOW class to create function calls      
pygameWindow = PYGAME_WINDOW()

print(pygameWindow)
while True: # Run until the user shuts down the program
    frame = controller.frame() # Create a frame object for hand detection
    if (len(frame.hands) > 0): # If the list of hand objects being detected
        # within the current frame is greater than zero, print 'hand detected.'
        print "hand detected."
    pygameWindow.Prepare() # Creates user window 
    pygameWindow.Draw_Black_Circle(x, y) # Draw the black dot to the screen
    Perturb_Circle_Position() # Randomly change dot position 
    pygameWindow.Reveal() # Update window frame 


