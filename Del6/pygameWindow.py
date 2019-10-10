import pygame # pygame module 
import constants # Contains all constant variables within the program

class PYGAME_WINDOW:
    # Function to initialize the window screen to a specific width/depth
    # for the UI window 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowWidth,
                                               constants.pygameWindowDepth))
    # Function to fill the window with a white background
    def Prepare(self):
        self.screen.fill((255, 255, 255))

    # Function that consistently updates the current window frame 
    def Reveal(self):
        pygame.display.update()

    # Function to draw a black circle given a specific (x,y) coordinate
    # within the users window 
    def Draw_Black_Circle(self, x, y):
        pygame.draw.circle(self.screen, (0,0,0), (x, y), 20)

    def Draw_Black_Line(self, xBase, yBase, xTip, yTip, fingerWidth):
        pygame.draw.line(self.screen, (0, 0, 0), (xBase, yBase), (xTip, yTip), fingerWidth)
