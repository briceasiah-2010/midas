import pygame
pygame.init()

screen=pygame.display.set_mode((600,600))
MIDAS_SIZE=50

midas_y=300
midas_x=300
midas_dy=0
midas_dx=0
speed=1

clock=pygame.time.Clock()


game_on=True
while game_on:
    screen.fill("white")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on=False
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_UP:
                midas_dy=-speed*MIDAS_SIZE
                midas_dx=0
            if event.key==pygame.K_DOWN:
                midas_dx=0
                midas_dy=speed*MIDAS_SIZE
            if event.key==pygame.K_RIGHT:
                midas_dy=0
                midas_dx=speed*MIDAS_SIZE
            if event.key==pygame.K_LEFT:
                midas_dx=-speed*MIDAS_SIZE
                midas_dy=0

    midas_rect=pygame.draw.rect(screen,"blue",(midas_x,midas_y,MIDAS_SIZE,MIDAS_SIZE))
    square_rect1=pygame.draw.rect(screen,"green",(50,20,MIDAS_SIZE,MIDAS_SIZE))
    square_rect2=pygame.draw.rect(screen,"green",(500,20,MIDAS_SIZE,MIDAS_SIZE))
    square_rect3=pygame.draw.rect(screen,"red",(20,500,MIDAS_SIZE,MIDAS_SIZE))
    square_rect4=pygame.draw.rect(screen,"red",(500,500,MIDAS_SIZE,MIDAS_SIZE))

    #midas_color="blue"
    if midas_rect.colliderect(square_rect1) or midas_rect.colliderect(square_rect2) or midas_rect.colliderect(square_rect3) or midas_rect.colliderect(square_rect4):
        midas_color="gold"

    midas_x=midas_x+midas_dx
    midas_y=midas_y+midas_dy

    #pygame.draw.rect(screen,"blue",(300,300,50,50))
    pygame.draw.rect(screen,"red",(50,20,50,50))
    #pygame.draw.rect(screen,"green",(500,20,50,50))
    pygame.draw.rect(screen,"silver",(20,500,50,50))
    pygame.draw.rect(screen,"yellow",(500,500,50,50))
    pygame.display.flip()
    clock.tick(9)
pygame.quit()