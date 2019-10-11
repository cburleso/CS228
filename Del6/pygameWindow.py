import pygame  
import constants 

class PYGAME_WINDOW:

    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((constants.pygameWindowWidth,
                                               constants.pygameWindowDepth))
    def Prepare(self):
        self.screen.fill((255, 255, 255))
        
    def Reveal(self):
        pygame.display.update()

    def Draw_Black_Circle(self, x, y):
        pygame.draw.circle(self.screen, (0,0,0), (x, y), 20)

    def Draw_Black_Line(self, xBase, yBase, xTip, yTip, fingerWidth):
        pygame.draw.line(self.screen, (0, 0, 0), (xBase, yBase), (xTip, yTip), fingerWidth)

    def drawHandImage(self):
        handImg = pygame.image.load('handOverDevice.jpg')
        self.screen.blit(handImg, (constants.pygameWindowWidth - 400, 0))

    def promptHandLeft(self):
        handImg = pygame.image.load('moveLeft.png')
        self.screen.blit(handImg, (constants.pygameWindowWidth - 400, 0))

    def promptHandRight(self):
        handImg = pygame.image.load('moveRight.png')
        self.screen.blit(handImg, (constants.pygameWindowWidth - 400, 0))

    def promptHandUp(self):
        handImg = pygame.image.load('moveUp.png')
        self.screen.blit(handImg, (constants.pygameWindowWidth - 400, 0))

    def promptHandDown(self):
        handImg = pygame.image.load('moveDown.png')
        self.screen.blit(handImg, (constants.pygameWindowWidth - 400, 0))

    def promptGreenCheck(self):
        handImg = pygame.image.load('greenCheck.png')
        self.screen.blit(handImg, (constants.pygameWindowWidth - 460, 0))
