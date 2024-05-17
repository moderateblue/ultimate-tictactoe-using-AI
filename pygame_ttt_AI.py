import pygame
import time

from tic_tac_toe_class import TicTacToe

from learning import UltimateTicTacToe, Agent, load_model

# Load the trained model and initialize the replay_buffer
model = load_model("tic_tac_toe_model_final.pth")
agent = Agent(model)
ttt_game = UltimateTicTacToe()

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

def reset():
    global grid_colors
    grid_colors = [AQUAMARINE, AQUAMARINE, AQUAMARINE,
                   AQUAMARINE, AQUAMARINE, AQUAMARINE,
                   AQUAMARINE, AQUAMARINE, AQUAMARINE]
    
    ttt_game.reset()
    ttt_game.current_player = 1
    
    global pieces
    pieces = pygame.Surface(window, pygame.SRCALPHA)

reset()

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

def calc_coords(x, y):
    big_x = x // 240
    big_y = y // 240
    #print(big_x, big_y)
    x = x % 240 - 9
    y = y % 240 - 9
    small_x = x // 74
    small_y = y // 74
    #print(small_x, small_y)
    large_coord = big_x + 1 + big_y * 3
    small_coord = small_x + 1 + small_y * 3
    #print(large_coord, small_coord)
    return large_coord, small_coord

#run game
run = True
#game active (no win or draw yet)
game = True

big_win = 0

while run:
    font = pygame.font.Font("Product Sans Regular.ttf", 50)

    #finish button
    r_text = font.render("Restart", True, GRAY)
    r_textRect = r_text.get_rect()
    r_textRect.center = (720 + 111, 720 // 2 + 222)
    #worried about blocking mouse clicks when game ends

    if ttt_game.current_player == 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    print(pos)

                    x = pos[0]
                    y = pos[1]

                    if game == True and ((x > 9 and x < 231) or (x > 249 and x < 471) or (x > 489 and x < 711)) and ((y > 9 and y < 231) or (y > 249 and y < 471) or (y > 489 and y < 711)):
                        
                        global large_coord, small_coord
                        large_coord, small_coord = calc_coords(x, y)

                        #large and small coord start at 1
                            #necessary for determining where to draw
                            #but ult_board and array index start at 0

                        if ttt_game.is_valid_move(large_coord-1, small_coord-1):
                            draw_x(large_coord, small_coord)
                            ttt_game.make_move(large_coord-1, small_coord-1)
                            print(ttt_game.prev_small_spot)

                        if ttt_game.prev_small_spot == -1:
                            grid_colors = [TRANSPARENT if ttt_game.main_board[x].won_by != 0 else AQUAMARINE for x in range(9)]
                        else:
                            grid_colors = [TRANSPARENT for x in range(9)]
                            grid_colors[ttt_game.prev_small_spot] = AQUAMARINE
                        
                        big_win = ttt_game.check_winner()
                        if big_win != 0:
                            game = False
                            ttt_game.current_player = 1
                            #pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
                            grid_colors = [TRANSPARENT for x in range(9)]

                    elif x >= 756 and x <= 910 and y >= 565 and y <= 601:
                        game = True
                        reset()
    
    elif game:
        valid_moves = ttt_game.get_valid_moves()
        #time.sleep(1)
        action = agent.select_action(ttt_game.get_state(), valid_moves)
        board_index, cell_index = divmod(action, 9)
        if ttt_game.make_move(board_index, cell_index):
            draw_o(board_index+1, cell_index+1)
            print("Agent made a move.")
        else:
            print("Agent made an invalid move. Something went wrong.")
            game = False

        if ttt_game.prev_small_spot == -1:
            grid_colors = [TRANSPARENT if ttt_game.main_board[x].won_by != 0 else AQUAMARINE for x in range(9)]
        else:
            grid_colors = [TRANSPARENT for x in range(9)]
            grid_colors[ttt_game.prev_small_spot] = AQUAMARINE
        
        big_win = ttt_game.check_winner()
        if big_win != 0:
            game = False
            #pygame.event.set_blocked(pygame.MOUSEBUTTONDOWN)
            grid_colors = [TRANSPARENT for x in range(9)]


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

    text = None
    if big_win != 3 and big_win != 0:
        text = font.render("X won!" if big_win == 1 else "O won!", True, GRAY)
    elif big_win == 3:
        text = font.render("Tie!", True, GRAY)
    else:
        text = font.render("X's turn" if ttt_game.current_player == 1 else "O's turn", True, GRAY)
    textRect = text.get_rect()

    # set the center of the rectangular object.
    textRect.center = (720 + 111, 720 // 2)

    sboards.blit(pieces, (0, 0))
    sboards.blit(lines, (0, 0))
    screen.blit(sboards, (0, 0))
    screen.blit(text, textRect)
    screen.blit(r_text, r_textRect)

    clock.tick(60)
    pygame.display.flip()

pygame.quit()