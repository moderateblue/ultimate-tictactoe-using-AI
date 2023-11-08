import pygame
import math

#from ult_ttt import *

#create pygame
pygame.init()

#initialize board
window = [720 + 222, 720]
clock = pygame.time.Clock()

screen = pygame.display.set_mode(window, pygame.RESIZABLE)
lines = pygame.Surface(window, pygame.SRCALPHA)
sboards = pygame.Surface(window, pygame.SRCALPHA)

#colors
CYAN = (20, 189, 172)
AQUAMARINE = (3, 252, 182)
BLACK = (0, 0, 0)
GRAY = (84, 84, 84)
WHITE = (242, 235, 211)

grid_colors = [AQUAMARINE, AQUAMARINE, AQUAMARINE,
               AQUAMARINE, AQUAMARINE, AQUAMARINE,
               AQUAMARINE, AQUAMARINE, AQUAMARINE]

#run game
run = True

toggle = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos)
                
                if toggle:
                    grid_colors[8] = WHITE
                    toggle = not toggle
                else:
                    grid_colors[8] = AQUAMARINE
                    toggle = not toggle
                sboards.blit(lines, (0, 0))
                screen.blit(sboards, (0, 0))

    screen.fill(CYAN)
    lines.fill((0, 0, 0, 0))
    sboards.fill((0, 0, 0, 0))



    #draws screen

    #margin is 9
    #each square is 222x222
    #each small square is 74 (no margin)
    #ex first row of pixels is 9 + 222 (= 74 * 3) + 9 + 9 + 222 + 9 + 9 + 222 + 9 = 720

    pygame.draw.line(lines, BLACK, [9 + 222 + 9, 9], [9 + 222 + 9, 711], width=5)
    pygame.draw.line(lines, BLACK, [27 + 444 + 9, 9], [27 + 444 + 9, 711], width=5)
    pygame.draw.line(lines, BLACK, [9, 9 + 222 + 9], [711, 9 + 222 + 9], width=5)
    pygame.draw.line(lines, BLACK, [9, 27 + 444 + 9], [711, 27 + 444 + 9], width=5)

    for i in range(3):
        for j in range(3):
            pygame.draw.rect(sboards, grid_colors[(i+1) * (j+1) - 1], [9 + 18 * j + 222 * j, 9 + 18 * i + 222 * i, 222, 222])
            pygame.draw.line(lines, BLACK, [9 + 74 + 240 * j, 9 + 240 * i], [9 + 74 + 240 * j, 9 + 240 * i + 222], width=3)
            pygame.draw.line(lines, BLACK, [9 + 148 + 240 * j, 9 + 240 * i], [9 + 148 + 240 * j, 9 + 240 * i + 222], width=3)
            pygame.draw.line(lines, BLACK, [9 + 240 * i, 9 + 74 + 240 * j], [9 + 240 * i + 222, 9 + 74 + 240 * j], width=3)
            pygame.draw.line(lines, BLACK, [9 + 240 * i, 9 + 148 + 240 * j], [9 + 240 * i + 222, 9 + 148 + 240 * j], width=3)   

    sboards.blit(lines, (0, 0))
    screen.blit(sboards, (0, 0))

    clock.tick(60)
    pygame.display.flip()

pygame.quit()