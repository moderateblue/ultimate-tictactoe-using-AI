import pygame
import math

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
YELLOW = (239, 255, 161)

grid_colors = [YELLOW, YELLOW, YELLOW,
               YELLOW, YELLOW, YELLOW,
               YELLOW, YELLOW, YELLOW]



#initialize global game variables

ult_board = []
for i in range(9):
    ult_board.append(TicTacToe(i))

#turn = True (X) False (O)
turn = True

#prev_small_spot = 0 if its wherever
#prev_small_spot actual range = (1-9)
prev_small_spot = 0



#run game
run = True

#test toggle
toggle = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                pos = pygame.mouse.get_pos()
                print(pos)

                x = pos[0]
                y = pos[1]

                if ((x > 9 and x < 231) or (x > 249 and x < 471) or (x > 489 and x < 711)) and ((y > 9 and y < 231) or (y > 249 and y < 471) or (y > 489 and y < 711)):
                    xs = x // 240
                    ys = y // 240
                    print(xs, ys)
                    x = x % 240 - 9
                    y = y % 240 - 9
                    xss = x // 74
                    yss = y // 74
                    print(xss, yss)
                    print((xs + 1) + ys * 3, (xss + 1) + yss * 3)
                
                if toggle:
                    grid_colors[8] = AQUAMARINE
                    toggle = not toggle
                else:
                    grid_colors[8] = YELLOW
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