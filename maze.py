from pygame import*

window = display.set_mode((700, 500))
display.set_caption("Ну давай, давай, нападай")
background = transform.scale(image.load('background.jpg'), (700, 500))
game = True
clock = time.Clock()
FPS = 60

class Game(sprite.Sprite):
    def __init__(self, image1, x, y, speed):
        super().__init__()
        self.image = transform.scale(image.load(image1), (50, 50)) 
        self.speed = speed
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def reset(self):
        window.blit(self.image,(self.rect.x, self.rect.y))

class Player(Game):
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

class Enemy(Game):
    def update(self):
        if self.rect.x >= 650:
            self.direction = 'left'
        if self.rect.x <= 500:
            self.direction = 'right'
        
        if self.direction == 'left':
            self.rect.x -= self.speed
        if self.direction == 'right':
            self.rect.x += self.speed

class Enemy2(Game):
    def update(self):
        if self.rect.y >= 650:
            self.direction = 'up'
        if self.rect.y <= 500:
            self.direction = 'down'
        
        if self.direction == 'up':
            self.rect.y -= self.speed
        if self.direction == 'down':
            self.rect.y += self.speed

class Wall(sprite.Sprite):
    def __init__(self, color_1, color_2, color_3, wall_x, wall_y, wall_widht, wall_height):
        super().__init__()
        self.color_1 = color_1
        self.color_2 = color_2
        self.color_3 = color_3
        self.width = wall_widht
        self.height = wall_height
        self.image = Surface((self.width, self.height))
        self.image.fill((color_1,color_2,color_3))
        self.rect = self.image.get_rect()
        self.rect.x = wall_x
        self.rect.y = wall_y

    def draw_wall(self):
        window.blit(self.image, (self.rect.x,self.rect.y))
w1 = Wall(255,0,0,100,100,100,100)


test1 = Player('hero.png', 0, 0, 5)

test2 = Enemy('cyborg.png', 300, 350, 5)

test3 = Game('treasure.png', 650, 450, 0)

test4 = Enemy2('cyborg.png', 650, 450, 5)

test5 = Wall(255, 255, 0, 50, 50, 50, 7)




font.init()
font = font.Font(None,70)
win = font.render('YOU WIN', True,(0,255,0))
lose = font.render('YOU LOSE', True,(255,0,0))









finish = False
mixer.init()
mixer.music.load('jungles.ogg')
money = mixer.Sound('money.ogg')

while game:
    for e in event.get():
        if e.type == QUIT:
            game = False
    if test1.rect.x == 950 and test1.rect.y == 750:
        money.play()
    if finish != True:
        window.blit(background,(0,0))
        test1.reset()
        test1.update()
        test2.reset()
        test2.update()
        test3.reset()
        test4.reset()
        test4.update()
        test5.draw_wall()
        mixer.music.play()
        test1.update()

    if sprite.collide_rect(test1,test2):
        finish = True
        window.blit(lose,(230,225))
    if sprite.collide_rect(test1,test3):
        finish = True
        window.blit(win,(230,225))


    display.update()
    clock.tick(FPS)
