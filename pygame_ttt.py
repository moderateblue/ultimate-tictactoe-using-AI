import pygame

from pygame_ttt_funcs import TicTacToe

#create pygame
pygame.init()

#initialize board
window = [720 + 222, 720]
clock = pygame.time.Clock()

screen = pygame.display.set_mode(window, pygame.RESIZABLE)
pygame.display.set_caption("Ultimate TicTacToe")
lines = pygame.Surface(window, pygame.SRCALPHA)
sboards = pygame.Surface(window, pygame.SRCALPHA)
pieces = pygame.Surface(window, pygame.SRCALPHA)

#colors
CYAN = (20, 189, 172)
DARKCYAN = (6, 84, 76)
AQUAMARINE = (8, 156, 140)
BLACK = (0, 0, 0)
GRAY = (84, 84, 84)
WHITE = (242, 235, 211)
TRANSPARENT = (0, 0, 0, 0)


grid_colors = [AQUAMARINE, AQUAMARINE, AQUAMARINE,
               AQUAMARINE, AQUAMARINE, AQUAMARINE,
               AQUAMARINE, AQUAMARINE, AQUAMARINE]

'''-------------------Game Code-------------------'''

#initialize global game variables

ult_board = []
for i in range(9):
    ult_board.append(TicTacToe(i))

#turn = True (X) False (O)
turn = True

#prev_small_spot = 0 if its wherever
#prev_small_spot actual range = (1-9)
prev_small_spot = 0

'''-----------------------------------------------'''

def draw_o(big, small):
    circlex = ((big - 1) % 3) * 240 + ((small - 1) % 3) * 74 + 9 + 37
    circley = ((big - 1) // 3) * 240 + ((small - 1) // 3) * 74 + 9 + 37
    pygame.draw.circle(pieces, WHITE, (circlex, circley), 30, 10)

def draw_x(big, small):
    #tl = top left, br = bottom right
    #tr = top right, bl = bottom left

    # +-5 is to make sure the line drew doesn't exceed the square
    # +-7 is to make the overall size smaller

    tl = (((big - 1) % 3) * 240 + ((small - 1) % 3) * 74 + 9 + (5 + 7) , ((big - 1) // 3) * 240 + ((small - 1) // 3) * 74 + 9 + (7))
    br = (((big - 1) % 3) * 240 + ((small - 1) % 3) * 74 + 9 + 74 - (5 + 7), ((big - 1) // 3) * 240 + ((small - 1) // 3) * 74 + 9 + 74 - (7))
    
    tr = (((big - 1) % 3) * 240 + ((small - 1) % 3) * 74 + 9 + 74 - (5 + 7), ((big - 1) // 3) * 240 + ((small - 1) // 3) * 74 + 9 + (7))
    bl = (((big - 1) % 3) * 240 + ((small - 1) % 3) * 74 + 9 + 5 + (7), ((big - 1) // 3) * 240 + ((small - 1) // 3) * 74 + 9 + 74 - (7))

    pygame.draw.line(pieces, GRAY, tl, br, 10)
    pygame.draw.line(pieces, GRAY, tr, bl, 10)

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
                    big_x = x // 240
                    big_y = y // 240
                    print(big_x, big_y)
                    x = x % 240 - 9
                    y = y % 240 - 9
                    small_x = x // 74
                    small_y = y // 74
                    print(small_x, small_y)
                    global large_coord, small_coord
                    large_coord = big_x + 1 + big_y * 3
                    small_coord = small_x + 1 + small_y * 3
                    print(large_coord, small_coord)

                    if turn:
                        draw_x(large_coord, small_coord)
                    else:
                        draw_o(large_coord, small_coord)
                
                if toggle:
                    grid_colors[0:8] = [TRANSPARENT for x in grid_colors[0:8]]
                    print(grid_colors)
                    toggle = not toggle
                else:
                    grid_colors[0:8] = [AQUAMARINE for x in grid_colors[0:8]]
                    toggle = not toggle
                turn = not turn

        sboards.blit(lines, (0, 0))
        screen.blit(sboards, (0, 0))

    screen.fill(CYAN)
    lines.fill((0, 0, 0, 0))
    sboards.fill((0, 0, 0, 0))



    #draws screen

    #margin is 9
    #each square is 222x222 (no margin)
    #each small square is 74 (no margin)
    #ex first row of pixels is 9 + 222 (= 74 * 3) + 9 + 9 + 222 + 9 + 9 + 222 + 9 = 720

    pygame.draw.line(lines, DARKCYAN, [9 + 222 + 9, 9], [9 + 222 + 9, 711], width=5)
    pygame.draw.line(lines, DARKCYAN, [27 + 444 + 9, 9], [27 + 444 + 9, 711], width=5)
    pygame.draw.line(lines, DARKCYAN, [9, 9 + 222 + 9], [711, 9 + 222 + 9], width=5)
    pygame.draw.line(lines, DARKCYAN, [9, 27 + 444 + 9], [711, 27 + 444 + 9], width=5)

    for i in range(3):
        for j in range(3):
            pygame.draw.rect(sboards, grid_colors[(i+1) * (j+1) - 1], [9 + 18 * j + 222 * j, 9 + 18 * i + 222 * i, 222, 222])
            pygame.draw.line(lines, DARKCYAN, [9 + 74 + 240 * j, 9 + 240 * i], [9 + 74 + 240 * j, 9 + 240 * i + 222], width=3)
            pygame.draw.line(lines, DARKCYAN, [9 + 148 + 240 * j, 9 + 240 * i], [9 + 148 + 240 * j, 9 + 240 * i + 222], width=3)
            pygame.draw.line(lines, DARKCYAN, [9 + 240 * i, 9 + 74 + 240 * j], [9 + 240 * i + 222, 9 + 74 + 240 * j], width=3)
            pygame.draw.line(lines, DARKCYAN, [9 + 240 * i, 9 + 148 + 240 * j], [9 + 240 * i + 222, 9 + 148 + 240 * j], width=3)   

    
    font = pygame.font.Font("Product Sans Regular.ttf", 50)
    text = font.render("X's turn" if turn == True else "O's turn", True, GRAY)
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (720 + 111, 720 // 2)

    sboards.blit(pieces, (0, 0))
    sboards.blit(lines, (0, 0))
    screen.blit(sboards, (0, 0))
    screen.blit(text, textRect)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()