import pygame
from random import randrange
#pygame.init()
window=800
title_size=50
Range=(title_size//2,window-title_size//2,title_size)
get_random_position=lambda:[randrange(*Range),randrange(*Range)]
snake=pygame.Rect([0,0,title_size-2,title_size-2])
snake.center=get_random_position()
pygame.display.set_caption('SnakEat')

l=1
r=True
segments=[snake.copy()]
s=pygame.display.set_mode([window]*2)
clck=pygame.time.Clock()
snake_dir=(0,0)
time,time_step=0,200
food= snake.copy()
food.center=get_random_position()
while r== True:
    for event in pygame.event.get():
        if event.type== pygame.QUIT:
            r=False
        if event.type== pygame.KEYDOWN:
            if event.key== pygame.K_w:
                snake_dir=(0,-title_size)
            elif event.key== pygame.K_s:
                snake_dir=(0,title_size)
            elif event.key== pygame.K_a:
                snake_dir=(-title_size,0)
            elif event.key== pygame.K_d:
                snake_dir=(title_size,0)
               
                
    s.fill((85,120,60))
    if snake.left<0 or snake.right> window or snake.top<0 or snake.bottom>window:
        snake.center,food.center=get_random_position(),get_random_position()
        l,snake_dir=1,(0,0)#check for hit
        segments=[snake.copy()]
    if snake.center ==food.center:#check food
        food.center= get_random_position()
        l+=1
    [pygame.draw.rect(s,(46,80,144),segment)for segment in segments] # draw snake
    pygame.draw.rect(s,(255,220,53),food) #draw food
    time_n=pygame.time.get_ticks()
    if time_n-time>time_step:
        time=time_n
        snake.move_ip(snake_dir)
        segments.append(snake.copy())
        segments = segments[-l:]
    pygame.display.flip()
    clck.tick(60)

pygame.quit()            
