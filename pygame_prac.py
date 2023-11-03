import pygame
import math

pygame.init()

window = [720, 720]
screen = pygame.display.set_mode(window)


CYAN = (28, 170, 156)

screen.fill(CYAN)

#margin is 9
#each small square is 222x222


pygame.draw.line(screen, (0, 0, 0), [9 + 222 + 9, 9], [9 + 222 + 9, 711], width=5)
pygame.draw.line(screen, (0, 0, 0), [27 + 444 + 9, 9], [27 + 444 + 9, 711], width=5)
pygame.draw.line(screen, (0, 0, 0), [9, 9 + 222 + 9], [711, 9 + 222 + 9], width=5)
pygame.draw.line(screen, (0, 0, 0), [9, 27 + 444 + 9], [711, 27 + 444 + 9], width=5)

for i in range(3):
    for j in range(3):
        pygame.draw.rect(screen, (3, 252, 182), [9 + 18 * j + 222 * j, 9 + 18 * i + 222 * i, 222, 222])
        pygame.draw.line(screen, (0, 0, 0), [9 + 74 + 240 * j, 9 + 240 * i], [9 + 74 + 240 * j, 9 + 240 * i + 222], width=3)
        pygame.draw.line(screen, (0, 0, 0), [9 + 148 + 240 * j, 9 + 240 * i], [9 + 148 + 240 * j, 9 + 240 * i + 222], width=3)
        pygame.draw.line(screen, (0, 0, 0), [9 + 240 * i, 9 + 74 + 240 * j], [9 + 240 * i + 222, 9 + 74 + 240 * j], width=3)
        pygame.draw.line(screen, (0, 0, 0), [9 + 240 * i, 9 + 148 + 240 * j], [9 + 240 * i + 222, 9 + 148 + 240 * j], width=3)

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            print(pos)

    pygame.display.flip()

pygame.quit()