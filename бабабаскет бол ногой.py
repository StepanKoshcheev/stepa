from pygame import *
from random import *
font.init()
font2 = font.Font(None, 40)
window = display.set_mode((700,500))
background = transform.scale(image.load('galaxy.jpg'),(700,500))
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

lox = 0
class Player(Game):
    def fire(self):
        keys = key.get_pressed()
        if keys[K_SPACE]:
            bulet = Bulet('bullet.png',ship.rect.x,ship.rect.y,20,20 ,50)
            bulets.add(bulet)
    def update(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y>5:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y<500-50:
            self.rect.y += self.speed
        if keys[K_RIGHT] and self.rect.x<700-50:
            self.rect.x += self.speed
        if keys[K_LEFT] and self.rect.x>5:
            self.rect.x -= self.speed
lost = 0 
class Enemy(Game):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = randint(0,600)
            global lost
            lost += 1
class astr(Game):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = 365
            global lost
            lost += 1
class astr1(Game):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = -1
            self.rect.x = 476
            global lost
            lost += 1
class astr11(Game):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = 0
            self.rect.x = 245
            global lost
            lost += 1
class astr111(Game):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 500:
            self.rect.y = -1
            self.rect.x = 143
            global lost
            lost += 1
class Bulet(Game):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
Astr = sprite.Group()
Astr1 = sprite.Group()
Astr11 = sprite.Group()
Astr111 = sprite.Group()
monsters = sprite.Group()
bulets = sprite.Group()
for i in range(0,6):
    monster = Enemy('ufo.png',randint(0,600), 0,50 , 50, randint(1,5))
    monsters.add(monster)
for i in range(0,3):
    ast = astr('asteroid.png',365, 0,50 , 50, 3)
    Astr.add(ast)
    ast1 = astr('asteroid.png',365, -1,50 , 50, 3)
    Astr.add(ast1)
x = randint(2,5)
for i in range(0,3):
    
    ast = astr1('asteroid.png',476, 0,50 , 50, x)
    Astr1.add(ast)
    ast1 = astr1('asteroid.png',476, -1,50 , 50, x)
    Astr1.add(ast1)

for i in range(0,3):
    ast = astr11('asteroid.png',245, 0,50 , 50, 5)
    Astr11.add(ast)
    ast1 = astr11('asteroid.png',245, -1,50 , 50, 5)
    Astr11.add(ast1)

for i in range(0,3):
    ast = astr111('asteroid.png',143, 0,50 , 50, 4)
    Astr111.add(ast)
    ast1 = astr111('asteroid.png',143, -1,50 , 50, 4)
    Astr111.add(ast1)

finish = False
ship = Player('rocket.png',350,450,50,50,15) 
mixer.init()
mixer.music.load('space.ogg')
while game:
    for e in event.get():
        if e.type == QUIT: 
            game = False
                
    window.blit(background,(0,0))
    text = font2.render("Пpопущено:"+str(lost), True,(255,255,255))
    text2 = font2.render("попал:"+str(lox), True,(255,255,255))
    window.blit(text,(0,0))
    window.blit(text2,(200,0))
    if lost >= 250:
        finish = True
        text3 = font2.render("ВЫ ПРОИГРАЛИ:(",True, (0,255,0))
        window.blit(text3,(110,110))
    
    if not finish:
        Astr.update()
        Astr.draw(window)
        Astr1.update()
        Astr1.draw(window)
        Astr11.update()
        Astr11.draw(window)
        Astr111.update()
        Astr111.draw(window)
        ship.update()
        ship.reset()
        monsters.update()
        monsters.draw(window)
        bulets.update()
        bulets.draw(window)
        ship.fire()

        sprite_list = sprite.spritecollide(ship, monsters, True)
        if sprite_list:
            monster = Enemy('ufo.png',randint(0,600), 0, 50, 50,randint(1,5))
            monsters.add(monster)

        sprite_list2 = sprite.groupcollide(bulets, monsters, False, True)
        if sprite_list2:
            
            lox +=1
            monsters.add(monster)
            monster = Enemy('ufo.png',randint(0,600), 0,50,50,randint(1,5))
            monsters.add(monster)
        
        sprite_list3 = sprite.groupcollide(bulets, Astr, True, True)
        if sprite_list3:
            
            ast = astr('asteroid.png',365, 0,50 , 50, 3)
            Astr.add(ast)
            ast1 = astr('asteroid.png',365, -10,50 , 50, 3)
            Astr.add(ast1)
        sprite_list3 = sprite.groupcollide(bulets, Astr1, True, True)
        if sprite_list3:
            
            ast = astr1('asteroid.png',476, 0,50 , 50, x)
            Astr1.add(ast)
            ast1 = astr1('asteroid.png',476, -10,50 , 50, x)
            Astr1.add(ast1)
    display.update() 
    time.delay(60)