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

    def promptASLnum(self, mode):
        if mode == 0:
            pic = pygame.image.load('0.png')
        elif mode == 1:
            pic = pygame.image.load('1.png')
        elif mode == 2:
            pic = pygame.image.load('2.png')
        elif mode == 3:
            pic = pygame.image.load('3.png')
        elif mode == 4:
            pic = pygame.image.load('4.png')
        elif mode == 5:
            pic = pygame.image.load('5.png')
        elif mode == 6:
            pic = pygame.image.load('6.png')
        elif mode == 7:
            pic = pygame.image.load('7.png')
        elif mode == 8:
            pic = pygame.image.load('8.png')
        else:
            pic = pygame.image.load('9.png')
            
        pic = pygame.transform.scale(pic, (375,375))
        self.screen.blit(pic, (375,375))
       
            
    def promptASLsign(self, mode):
        if mode == 0:
            pic = pygame.image.load('asl0.png')
        elif mode == 1:
            pic = pygame.image.load('asl1.png')
        elif mode == 2:
            pic = pygame.image.load('asl2.png')
        elif mode == 3:
            pic = pygame.image.load('asl3.png')
        elif mode == 4:
            pic = pygame.image.load('asl4.png')
        elif mode == 5:
            pic = pygame.image.load('asl5.png')
        elif mode == 6:
            pic = pygame.image.load('asl6.png')
        elif mode == 7:
            pic = pygame.image.load('asl7.png')
        elif mode == 8:
            pic = pygame.image.load('asl8.png')
        else:
            pic = pygame.image.load('asl9.png')

        pic = pygame.transform.scale(pic, (375,375))
        self.screen.blit(pic, (375,0))
        
