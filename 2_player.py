#02/11/24

import pygame,random

pygame.init()
sc = pygame.display.set_mode((700,600))
pygame.display.set_caption('Ship 1 vs Ship 2')

gameover = False
winner = ''
yellow_h = 100
red_h = 100
ship_sp = 3

bullet_sp = 8
yellow_b = []
red_b = []


yellow_s = pygame.image.load('yellow_ship.png')
yellow_s = pygame.transform.rotate(pygame.transform.scale(yellow_s,(50,50)),90)

red_s = pygame.image.load('red_ship.png')
red_s = pygame.transform.rotate(pygame.transform.scale(red_s,(50,50)),-90)

back = pygame.image.load('space_back.png')
back = pygame.transform.scale(back,(700,600))

border = pygame.Rect(345,0,10,600)
yellow_r = pygame.Rect(175,275,50,50)
red_r = pygame.Rect(575,275,50,50)

def draw_window():
    sc.blit(back,(0,0))
    
    pygame.draw.rect(sc,'grey',border)
    
    font = pygame.font.SysFont('comfortaa',40)
    yellow_txt = font.render(f'Health: {yellow_h}',True,'light green')
    red_txt = font.render(f'Health: {red_h}',True,'light green')
    gameover_txt = font.render(f'The winner is {winner}!!!',True,'red')

    sc.blit(yellow_txt,(50,50))
    sc.blit(red_txt,(500,50))
    sc.blit(yellow_s,(yellow_r.x,yellow_r.y))
    sc.blit(red_s,(red_r.x,red_r.y))

    if gameover:
        sc.clear()
        sc.fill('dark green')
        sc.blit(gameover_txt,True,'black')     

    for i in red_b:
        pygame.draw.rect(sc,'red',i)

    for i in yellow_b:
        pygame.draw.rect(sc,'dark yellow',i)

def red_move(keys):
    if keys[pygame.K_i] and red_r.y>0:
        red_r.y-= ship_sp
    if keys[pygame.K_j] and red_r.x>355:
        red_r.x-= ship_sp
    if keys[pygame.K_l] and red_r.x<650:
        red_r.x+= ship_sp
    if keys[pygame.K_k] and red_r.y<550:
        red_r.y+= ship_sp

def yellow_move(keys):
    if keys[pygame.K_w] and yellow_r.y>0:
        yellow_r.y-= ship_sp
    if keys[pygame.K_a] and yellow_r.x>0:
        yellow_r.x-= ship_sp
    if keys[pygame.K_d] and yellow_r.x<295:
        yellow_r.x+= ship_sp
    if keys[pygame.K_s] and yellow_r.y<550:
        yellow_r.y+= ship_sp

def bullet_move(yellow_b,red_b):
    global red_h,yellow_h,bullet_sp
    for i in yellow_b:
        i.x+=bullet_sp
        if red_r.colliderect(i):
            red_h-=10
            yellow_b.remove(i)
        elif i.x>700:
            yellow_.remove(i)

    for i in red_b:
        i.x-=bullet_sp
        if yellow_r.colliderect(i):
            yellow_h-=10
            yellow_b.remove(i)
        elif i.x<0:
            yellow_b.remove(i)
            
def gameover2():
    global red_h,yellow_h
    if red_h==0:
        winner = 'the yellow ship'
        gameover = True

    elif yellow_h==0:
        winner = 'the red ship'
        gameover = True

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_q:
                bullet = pygame.Rect(yellow_r.x+25,yellow_r.y+25,10,10)
                yellow_b.append(bullet)
            if event.key == pygame.K_u:
                bullet = pygame.Rect(red_r.x-25,red_r.y+25,10,10)
                red_b.append(bullet)
    draw_window()
    keys = pygame.key.get_pressed()
    red_move(keys)
    yellow_move(keys)
    bullet_move(yellow_b,red_b)
    gameover2()


    pygame.display.update()







