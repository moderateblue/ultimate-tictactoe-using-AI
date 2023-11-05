import pygame
import math

#create pygame
pygame.init()

#initialize board
window = [720, 720]
clock = pygame.time.Clock()

screen = pygame.display.set_mode(window)
lines = pygame.Surface(window, pygame.SRCALPHA)
sboards = pygame.Surface(window, pygame.SRCALPHA)

CYAN = (28, 170, 156)

screen.fill(CYAN)
lines.fill((0, 0, 0, 0))
sboards.fill((0, 0, 0, 0))

#margin is 9
#each small square is 222x222

pygame.draw.line(lines, (0, 0, 0), [9 + 222 + 9, 9], [9 + 222 + 9, 711], width=5)
pygame.draw.line(lines, (0, 0, 0), [27 + 444 + 9, 9], [27 + 444 + 9, 711], width=5)
pygame.draw.line(lines, (0, 0, 0), [9, 9 + 222 + 9], [711, 9 + 222 + 9], width=5)
pygame.draw.line(lines, (0, 0, 0), [9, 27 + 444 + 9], [711, 27 + 444 + 9], width=5)

rect = []

for i in range(3):
    for j in range(3):
        rect.append(pygame.draw.rect(sboards, (3, 252, 182), [9 + 18 * j + 222 * j, 9 + 18 * i + 222 * i, 222, 222]))
        pygame.draw.line(lines, (0, 0, 0), [9 + 74 + 240 * j, 9 + 240 * i], [9 + 74 + 240 * j, 9 + 240 * i + 222], width=3)
        pygame.draw.line(lines, (0, 0, 0), [9 + 148 + 240 * j, 9 + 240 * i], [9 + 148 + 240 * j, 9 + 240 * i + 222], width=3)
        pygame.draw.line(lines, (0, 0, 0), [9 + 240 * i, 9 + 74 + 240 * j], [9 + 240 * i + 222, 9 + 74 + 240 * j], width=3)
        pygame.draw.line(lines, (0, 0, 0), [9 + 240 * i, 9 + 148 + 240 * j], [9 + 240 * i + 222, 9 + 148 + 240 * j], width=3)   

sboards.blit(lines, (0, 0))
screen.blit(sboards, (0, 0))

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
                    rect[8] = pygame.draw.rect(sboards, (255, 255, 255), [9 + 18 * j + 222 * j, 9 + 18 * i + 222 * i, 222, 222])
                    toggle = not toggle
                else:
                    rect[8] = pygame.draw.rect(sboards, (3, 252, 182), [9 + 18 * j + 222 * j, 9 + 18 * i + 222 * i, 222, 222])
                    toggle = not toggle
                sboards.blit(lines, (0, 0))
                screen.blit(sboards, (0, 0))

    clock.tick(60)
    pygame.display.flip()

pygame.quit()