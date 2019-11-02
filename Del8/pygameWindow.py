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
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('+', True, (0, 255, 0))
        self.screen.blit(text, (520, 150))
        # Coin visual
        coinImg = pygame.image.load('goldCoin.png')
        coinImg = pygame.transform.scale(coinImg, (50, 50))
        self.screen.blit(coinImg, (540, 140))

    def promptThumbsUp(self):
        handImg = pygame.image.load('thumbsUp.png')
        handImg = pygame.transform.scale(handImg, (325,325))
        self.screen.blit(handImg, (constants.pygameWindowWidth - 350, 0))

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

    def promptNumSeen(self, numSeen):
        # Eye visual
        eyeImg = pygame.image.load('eye.jpg')
        eyeImg = pygame.transform.scale(eyeImg, (130, 130))
        self.screen.blit(eyeImg, (0, 470))
        # Digit (# seen) visual
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('x' + str(numSeen), True, (0, 0, 0))
        self.screen.blit(text, (120, 538))

    def promptNumSuccess(self, numSuccess):
        # Green check visual
        checkImg = pygame.image.load('greenCheck.png')
        checkImg = pygame.transform.scale(checkImg, (160, 160))
        self.screen.blit(checkImg, (140, 470))
        # Digit (# successes) visual
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('x' + str(numSuccess), True, (0, 0, 0))
        self.screen.blit(text, (250, 538))
        

    def promptCurrCoinBag(self, numCoins):
        # Money bag check visual
        bagImg = pygame.image.load('moneyBag.jpg')
        bagImg = pygame.transform.scale(bagImg, (90, 70))
        self.screen.blit(bagImg, (0, 600))
        # Coin visual
        coinImg = pygame.image.load('goldCoin.png')
        coinImg = pygame.transform.scale(coinImg, (50, 50))
        self.screen.blit(coinImg, (120, 610))
        # Digit (# coins) visual
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render('x' + str(numCoins), True, (0, 0, 0))
        self.screen.blit(text, (175, 630))
        # Colon between coin pic and number
        font2 = pygame.font.Font('freesansbold.ttf', 32)
        text2 = font2.render(':', True, (0, 0, 0))
        self.screen.blit(text2, (95, 618))

    def promptPrevCoins(self, prevNumCoins):
        font = pygame.font.Font('freesansbold.ttf', 16)
        text = font.render('Coins Prev. Session:', True, (0, 0, 0))
        self.screen.blit(text, (230, 615))
        font2 = pygame.font.Font('freesansbold.ttf', 32)
        text2 = font2.render(str(prevNumCoins), True, (255, 0, 0))
        self.screen.blit(text2, (285, 635))

    def promptFlame(self):
        flameImg = pygame.image.load('flame.jpg')
        flameImg = pygame.transform.scale(flameImg, (75, 120))
        self.screen.blit(flameImg, (345, 458))

    def promptIce(self):
        iceImg = pygame.image.load('ice.png')
        iceImg = pygame.transform.scale(iceImg, (140, 120))
        self.screen.blit(iceImg, (295, 470))
        
        
        
