import pygame

from tic_tac_toe_class import TicTacToe

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

def check_big_win():
    winner = 'X'

    #rows
    for i in range(0, 9, 3):
        if (ult_board[i].won_by == winner) and (ult_board[i + 1].won_by == winner) and (ult_board[i + 2].won_by == winner):
            return (True, winner)

    #columns
    for i in range(3):
        if (ult_board[i].won_by == winner) and (ult_board[i + 3].won_by == winner) and (ult_board[i + 6].won_by == winner):
            return (True, winner)

    #top left to bottom right
    if (ult_board[0].won_by == winner and ult_board[4].won_by == winner and ult_board[8].won_by == winner):
        return (True, winner)

    #top right to bottom left
    elif (ult_board[2].won_by == winner and ult_board[4].won_by == winner and ult_board[6].won_by == winner):
        return (True, winner)
    
    winner = 'O'

    #rows
    for i in range(0, 9, 3):
        if (ult_board[i].won_by == winner) and (ult_board[i + 1].won_by == winner) and (ult_board[i + 2].won_by == winner):
            return (True, winner)

    #columns
    for i in range(3):
        if (ult_board[i].won_by == winner) and (ult_board[i + 3].won_by == winner) and (ult_board[i + 6].won_by == winner):
            return (True, winner)

    #top left to bottom right
    if (ult_board[0].won_by == winner and ult_board[4].won_by == winner and ult_board[8].won_by == winner):
        return (True, winner)

    #top right to bottom left
    elif (ult_board[2].won_by == winner and ult_board[4].won_by == winner and ult_board[6].won_by == winner):
        return (True, winner)

    else:
        global out_full
        out_full = False
        for i in range(9):
            if (ult_board[i].won_by != 0):
                out_full = True
            else:
                out_full = False
                break
        if (out_full):
            return (True, '-')
        return (False, 0)

def choose_big_spot(prev_small_spot):
    pass

def choose_small_spot(big, small):
    if (ult_board[big - 1].get(small-1) == ' ' and ult_board[big - 1].won_by == 0):
        ult_board[big - 1].change(small-1, 'X' if turn else 'O')
        ult_board[big - 1].check_small_win('X' if turn else 'O')
        global win_con
        win_con = check_big_win()
        if (win_con[0] and win_con[1] != '-'):
            print(win_con[1], "has won the game!")
            return
        elif (win_con[0] and win_con[1] == '-'):
            print("it's a tie!")
            return
        global prev_small_spot
        prev_small_spot = small

'''^^^^^^^^^^^^^^^^^^^Game Code^^^^^^^^^^^^^^^^^^^'''

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

big_win = (False, 0)

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

                    #large and small coord start at 1
                        #necessary for determining where to draw
                        #but ult_board and array index start at 0
                    if turn:
                        if (large_coord == prev_small_spot or prev_small_spot == 0) and ult_board[large_coord-1].get(small_coord-1) == ' ' and not ult_board[large_coord-1].won_by:
                            draw_x(large_coord, small_coord)
                            #turn = True (X) False (O)
                            ult_board[large_coord-1].change(small_coord-1, True)
                            ult_board[large_coord-1].check_small_win(True)

                            if ult_board[large_coord-1].won_by:
                                print("board complete")
                            prev_small_spot = small_coord

                            turn = not turn
                        
                    else:
                        if (large_coord == prev_small_spot or prev_small_spot == 0) and ult_board[large_coord-1].get(small_coord-1) == ' ' and not ult_board[large_coord-1].won_by:
                            draw_o(large_coord, small_coord)
                            #turn = True (X) False (O)
                            ult_board[large_coord-1].change(small_coord-1, False)
                            ult_board[large_coord-1].check_small_win(False)

                            if ult_board[large_coord-1].won_by:
                                print("board complete")
                            prev_small_spot = small_coord

                            turn = not turn
                    
                    if ult_board[prev_small_spot-1].won_by:
                        prev_small_spot = 0
                    
                    print("prev_small_spot", prev_small_spot)
                    
                    if prev_small_spot == 0:
                        grid_colors = [TRANSPARENT if ult_board[x].won_by in {'X', 'O', '-'} else AQUAMARINE for x in range(9)]
                    else:
                        grid_colors = [TRANSPARENT for x in range(9)]
                        grid_colors[prev_small_spot-1] = AQUAMARINE
                        print(grid_colors)
                    print(grid_colors)
                
                big_win = check_big_win()
                if big_win[0]:
                    pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                    grid_colors = [TRANSPARENT for x in range(9)]


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
            pygame.draw.rect(sboards, grid_colors[i * 3 + j], [9 + 18 * j + 222 * j, 9 + 18 * i + 222 * i, 222, 222])
            pygame.draw.line(lines, DARKCYAN, [9 + 74 + 240 * j, 9 + 240 * i], [9 + 74 + 240 * j, 9 + 240 * i + 222], width=3)
            pygame.draw.line(lines, DARKCYAN, [9 + 148 + 240 * j, 9 + 240 * i], [9 + 148 + 240 * j, 9 + 240 * i + 222], width=3)
            pygame.draw.line(lines, DARKCYAN, [9 + 240 * i, 9 + 74 + 240 * j], [9 + 240 * i + 222, 9 + 74 + 240 * j], width=3)
            pygame.draw.line(lines, DARKCYAN, [9 + 240 * i, 9 + 148 + 240 * j], [9 + 240 * i + 222, 9 + 148 + 240 * j], width=3)   

    
    font = pygame.font.Font("Product Sans Regular.ttf", 50)
    text = None
    if big_win[0] and big_win[1] in {"X", "O"}:
        text = font.render(f"{big_win[1]} won!", True, GRAY)
    elif big_win[0]:
        text = font.render("Tie!", True, GRAY)
    else:
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