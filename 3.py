import pygame
import time 
x = y = p = q = 0
running = 1
screen = pygame.display.set_mode((640, 400))
draw = False
screen.fill((0, 0, 0))

while running:
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        running = 0
    else:
        if event.type == pygame.MOUSEBUTTONDOWN:
            draw = True
        if event.type == pygame.MOUSEBUTTONUP:
            draw = False
        if event.type == pygame.MOUSEMOTION:
            if draw == True:
                (p, q) = event.pos
                (x, y) = (p, q)
                pygame.draw.line(screen, (255, 255, 255), (x, y), (p, q), 8)

    pygame.display.flip()
    
