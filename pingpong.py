#создай игру "Лабиринт"!
from pygame import *
from random import randint
from time   import time as tm

class GameSprite(sprite.Sprite):
    def __init__(self, img, x, y, sizeX, sizeY, speed=0):
        super().__init__()
        self.img = transform.scale(image.load(img), (sizeX, sizeY))
        self.rect = self.img.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        mw.blit(self.img, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def __init__(self, img, sizeX, sizeY, speed=0, id=0):
        super().__init__(img, (maxX - sizeX)//2, maxY - sizeY, sizeX, sizeY, speed)  
        self.id = id    
    def keyProcessing(self):
        keys = key.get_pressed()
        if self.id == 1:
            if keys[K_W]:
                self.rect.y += self.speed
            if keys[K_S]:
                self.rect.y += self.speed
        else:
            if keys[K_UP]:
                self.rect.y += self.speed
            if keys[K_DOWN]:
                self.rect.y += self.speed

        if self.rect.y > (maxY - self.rect.height):
            self.rect.y = (maxY - self.rect.height)
        elif self.rect.y < 0:
            self.rect.y = 0


maxX = 1280
maxY = 720
score = 0
antiScore = 0
wallColor = (150, 200, 150)
mw = display.set_mode((maxX, maxY))
display.set_caption('PINGPONG')

#mixer.init()#инициализировать микшер
#mixer.music.load('space.ogg')#загрузить фоновую музыку
#mixer.music.play()#начать воспроизведение фоновой музыки
#fire = mixer.Sound('fire.ogg')#загрузить звук выстрела

game = True
clock = time.Clock()
#bg = GameSprite('galaxy.jpg', 0, 0, maxX, maxY)
playerL = Player('platforma1.png', 50, 50, 17)
playerR = Player('platforma2.png', 50, 50, 17)
bullets = list()
enemys = list()

font.init()###
sis.font_ = font.Font("Arial", 70)###


victoryL = font_.render('LEFT ONE, YOU WIN', True, (255, 0, 0))###
victoryR = font_.render('RIGHT ONE, YOU WIN', True, (255, 0, 0))###
gameRes = 0
while game:
    bg.reset()
    if gameRes == 0:
        playerL.keyProcessing()
        playerR.keyProcessing()
    elif gameRes == -1:
        mw.blit(gameOver, (maxX//2, maxY//2))
    else:
        mw.blit(victory, (maxX//2, maxY//2))
    for e in event.get():
        if e.type == QUIT:
            game = False
    scoreLabel = font_.render('SCORE: ' + str(score), True, (255, 255, 255))###
    antiScoreLabel = font_.render('antiSCORE: ' + str(antiScore), True, (255, 255, 255))###
    mw.blit(scoreLabel, (0, 0))
    mw.blit(antiScoreLabel, (0, 40))
    display.update()
    clock.tick(60)