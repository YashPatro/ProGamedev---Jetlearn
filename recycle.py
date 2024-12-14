#07/12/24

import pygame,random,time

pygame.init()
sc = pygame.display.set_mode((800,800))


class Bin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('recycle_bin.png'), (40, 60))
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 100
    
    def update(self, keys):
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= 1
        if keys[pygame.K_RIGHT] and self.rect.x < 760:
            self.rect.x += 1
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= 1
        if keys[pygame.K_DOWN] and self.rect.y < 740:
            self.rect.y += 1

class Recycle(pygame.sprite.Sprite):
    def __init__(self,recycled):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(recycled),(40,60))
        self.rect = self.image.get_rect()

class Non_recycle(pygame.sprite.Sprite):
    def __init__(self):     
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load('plastic_bag.png'),(60,60))
        self.rect = self.image.get_rect()

r_l = ['pencil.png','paper_bag.png','box.png']

r_g = pygame.sprite.Group()
nr_g = pygame.sprite.Group()
a_g = pygame.sprite.Group()

for i in range(20):
    item = Recycle(random.choice(r_l))
    item.rect.x = random.randint(30,670)
    item.rect.y = random.randint(30,670)
    r_g.add(item)
    a_g.add(item)


for i in range(15):
    non_item = Non_recycle()
    non_item.rect.x = random.randint(30,670)
    non_item.rect.y = random.randint(30,670)
    nr_g.add(non_item)
    a_g.add(non_item)



bin = Bin()
a_g.add(bin)

count = time.time()
score = 0
font = pygame.font.SysFont('Calibri',30)
score_txt = font.render(f'You have recycled {score} items!',True,'Red')
back = pygame.transform.scale(pygame.image.load('recycle_back.png'),(800,800))
clock = pygame.time.Clock()
gameover = False
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    clock.tick(150)
    timer = time.time()-count
            
    
    if timer >= 20:
        if score >= 17:
            sc.fill('sky blue')
            winner_txt = font.render('You won!',True,'dark green')
            sc.blit(winner_txt,(400,400))
        else:
            sc.fill('light yellow')
            fin_txt = font.render('Better Luck Next Time!!!',True,'Dark red')
            sc.blit(fin_txt,(400,400))    
    else:
        
        sc.blit(back, (0, 0))
        a_g.draw(sc)
        sc.blit(score_txt, (470, 50))

        timer_txt = font.render(str(round(timer)),True,'red')
        sc.blit(timer_txt,(70,50))
        keys = pygame.key.get_pressed()
        bin.update(keys)
        collide_recycle = pygame.sprite.spritecollide(bin, r_g, True)
        if collide_recycle:
            score += len(collide_recycle)
        collide_n_recycle = pygame.sprite.spritecollide(bin, nr_g, True)
        if collide_n_recycle:
            score -= len(collide_n_recycle) 
    
    score_txt = font.render(f'You have recycled {score} items!', True, 'Red')


   
   
    pygame.display.update()

if gameover:
    sc.clear()
    gameover_txt = font.render('You Lost!',True,'Red')
    sc.blit(gameover_txt,(400,400))
