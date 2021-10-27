import pygame
from paddle import Paddle
from ball import Ball
import random

def main():

    pygame.init()

    pygame.display.set_caption("Lab 3")

    width = 800
    height = 450
    velo = 1.0
    screen = pygame.display.set_mode((width,height))
    pygame.display.update()

    screen.fill((0,0,0))

    pygame.draw.rect(screen,(155,155,155),pygame.Rect((0, 0), (width, 20)))

    pygame.draw.rect(screen,(155,155,155),pygame.Rect((0, 0), (20, height)))

    pygame.draw.rect(screen,(155,155,155),pygame.Rect((0, height-20), (width, 20)))

    pygame.draw.rect(screen,(255,255,255),pygame.Rect((width-20, height/2), (20, 100))) #paddle

    x0 = width - (4 * Ball.radius)
    y0 = height // 2
    vx0 = -velo
    vy0 = random.random()
    fgcolor = pygame.Color("green")
    bgcolor = pygame.Color("black")


    #ball init
    b0 = Ball(x0, y0, vx0, vy0, screen, fgcolor, bgcolor)
    b0.show((0, 155, 0))

    pygame.display.update()

    # define a variable to control the main loop
    running = True
        
    # main loop
    while running:
        # event handling, gets all event from the event queue
        for event in pygame.event.get():
            # only do something if the event is of type QUIT
            if event.type == pygame.QUIT:
                # change the value to False, to exit the main loop
                running = False
            pygame.display.update()
            b0.update()

if __name__=="__main__":
    # call the main function
    main()



