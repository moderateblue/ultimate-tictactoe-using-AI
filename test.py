from learning import UltimateTicTacToe, Agent, load_model

# Load the trained model and initialize the replay_buffer
model = load_model("tic_tac_toe_model_final.pth")
agent = Agent(model)
game = UltimateTicTacToe()

# Now you can use this agent to play the game
def play_human_vs_agent(agent, game):
    game.reset()
    while not game.check_winner() and not game.is_full():
        print(game.board)  # Print the current state of the board
        if game.current_player == 1:
            print("Your turn (X)")
            board_index = int(input("Enter the sub-board index (0-8): "))
            cell_index = int(input("Enter the cell index (0-8): "))
            if game.make_move(board_index, cell_index):
                print("You made a move.")
            else:
                print("Invalid move. Try again.")
                continue
        else:
            print("Agent's turn (O)")
            valid_moves = game.get_valid_moves()
            action = agent.select_action(game.get_state(), valid_moves)
            board_index, cell_index = divmod(action, 9)
            if game.make_move(board_index, cell_index):
                print("Agent made a move.")
            else:
                print("Agent made an invalid move. Something went wrong.")
                break

    print(game.board)  # Print the final state of the board
    winner = game.check_winner()
    if winner == 0:
        print("It's a tie!")
    elif winner == 1:
        print("Congratulations! You won!")
    else:
        print("The agent wins!")

# Assuming 'agent' and 'game' are already initialized
play_human_vs_agent(agent, game)