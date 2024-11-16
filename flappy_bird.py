#16/11/24

import pygame,random

pygame.init()
clock = pygame.time.Clock()
sc = pygame.display.set_mode((800,800))


font = pygame.font.SysFont('Calibri',50)
back = pygame.image.load('backround_flappy.png')
floor = pygame.image.load('floor_flappy.png')
flying = False
gameover = False


class Bird(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.images = []
        self.index = 0
        self.counter = 0
        for i in range(1,4):
            bird = pygame.image.load(f'bird{i}.png')
            self.images.append(bird)
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x,y)
        self.v = 0
        self.clicked = False
        

    def update():
        if flying:
            self.v+=0.5
            if self.v>8:
                self.v = 8
            if self.rect.bottom<632:
                self.rect.y+=self.v
        if gameover == False:
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                self.v = -10
            if pygame.mouse.get_pressed()[0] == 0:
                self.clicked = False
            self.counter+=1
            if self.counter>5:
                self.index+=1
                if self.index>=3:
                    self.index = 0
                self.image = self.images[self.index]

bird_g = pygame.sprite.Group()
flappy = Bird(40,400)
bird_g.add(flappy)

while True:
   

        #if event.type == pygame.MOUSEBUTTONDOWN and flying == False and gameover == False:
           # flying = True
    
    
    clock.tick(60)
    sc.blit(back,(0,0))
    bird_g.draw(sc)
    bird_g.update()
    sc.blit(floor,(0,632))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()


    pygame.display.update()

