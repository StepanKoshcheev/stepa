from pygame import *
from random import *
font.init()
font2 = font.Font(None, 40)
window = display.set_mode((700,500))
background = transform.scale(image.load('zackat.png'),(700,500))
game = True
class Game(sprite.Sprite):
    def __init__(self, image1, x, y, size_x, size_y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image1), (size_x, size_y)) 
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        
    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player1(Game):
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<500-50:
            self.rect.y += self.speed

class Player2(Game):
    def update(self):
        keys = key.get_pressed()
        if keys[K_W] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_S] and self.rect.y<500-50:
            self.rect.y += self.speed

rackt = Player1('rackt.png', 350, 250, 25, 125, 15 )
rackt2 = Player2('')
while game:
    for e in event.get():
        if e.type == QUIT: 
            game = False
    window.blit(background,(0,0))
    rackt.reset()
    rackt.update()
    display.update() 
    time.delay(60)