# NOTES
# reworked entire coordinate system, now input is synchronized with index value (0-8) instead of (1-9)
# X now represented by 1 instead of "X"
# O now represented by 2 instead of "O"
# empty now represented by 0 instead of " "
# full/draw now represented by 3 instead of "-"

# check_big_win is now check_winner
# also returns a number instead of a list

# i have no idea what im doing

import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import random
from tic_tac_toe_class import TicTacToe

class UltimateTicTacToe:
    def __init__(self):
        self.board = [0] * 9
        self.current_player = 1
        self.main_board = []
        for i in range(9):
            self.main_board.append(TicTacToe(i))
        self.prev_small_spot = -1

    def reset(self):
        self.board = [0] * 9
        self.current_player = 1
        self.main_board = []
        for i in range(9):
            self.main_board.append(TicTacToe(i))
        self.prev_small_spot = -1

    def make_move(self, board_index, cell_index):
        if self.is_valid_move(board_index, cell_index):
            self.main_board[board_index].change(cell_index, self.current_player)
            self.main_board[board_index].check_small_win()
            self.prev_small_spot = cell_index
            if self.main_board[cell_index].won_by != 0:
                self.prev_small_spot = -1
            self.current_player = 3 - self.current_player
            return True
        return False

    def is_valid_move(self, board_index, cell_index):
        if self.prev_small_spot == -1:
            big_spot = board_index
            if (big_spot >= 0 and big_spot <= 8 and self.main_board[big_spot].won_by == 0):
                spot = cell_index
                if (spot >= 0 and spot <= 8 and self.main_board[big_spot].get(spot) == 0):
                    return True

        elif board_index == self.prev_small_spot:
            spot = cell_index
            big_spot = board_index
            if (spot >= 0 and spot <= 8 and self.main_board[big_spot].get(spot) == 0):
                return True
        
        return False

    # OBSOLETE FUNCTION
    # def update_board(self, board_index):
    #     sub_board = [self.main_board[board_index].get(i) for i in range(9)]

    #     for i in range(3):
    #         if sub_board[i * 3] == sub_board[i * 3 + 1] == sub_board[i * 3 + 2] != 0:
    #             self.board[board_index] = sub_board[i * 3]
    #         if sub_board[i] == sub_board[i + 3] == sub_board[i + 6] != 0:
    #             self.board[board_index] = sub_board[i]
    #     if sub_board[0] == sub_board[4] == sub_board[8] != 0:
    #         self.board[board_index] = sub_board[0]
    #     if sub_board[2] == sub_board[4] == sub_board[6] != 0:
    #         self.board[board_index] = sub_board[2]

    def check_winner(self):
        for winner in range(1, 3):

            #rows
            for i in range(0, 9, 3):
                if (self.main_board[i].won_by == winner) and (self.main_board[i + 1].won_by == winner) and (self.main_board[i + 2].won_by == winner):
                    return winner

            #columns
            for i in range(3):
                if (self.main_board[i].won_by == winner) and (self.main_board[i + 3].won_by == winner) and (self.main_board[i + 6].won_by == winner):
                    return winner

            #top left to bottom right
            if (self.main_board[0].won_by == winner and self.main_board[4].won_by == winner and self.main_board[8].won_by == winner):
                return winner

            #top right to bottom left
            elif (self.main_board[2].won_by == winner and self.main_board[4].won_by == winner and self.main_board[6].won_by == winner):
                return winner
        
        global out_full
        out_full = False
        for i in range(9):
            if (self.main_board[i].won_by != 0):
                out_full = True
            else:
                out_full = False
                break
        if (out_full):
            return 3
        
        # no winner yet
        return 0


        # OBSOLETE CODE
        # for i in range(3):
        #     if self.main_board[i * 3] == self.main_board[i * 3 + 1] == self.main_board[i * 3 + 2] != 0:
        #         return self.main_board[i * 3]
        #     if self.main_board[i] == self.main_board[i + 3] == self.main_board[i + 6] != 0:
        #         return self.main_board[i]
        # if self.main_board[0] == self.main_board[4] == self.main_board[8] != 0:
        #     return self.main_board[0]
        # if self.main_board[2] == self.main_board[4] == self.main_board[6] != 0:
        #     return self.main_board[2]
        # return 0

    def get_state(self):
        return [[self.main_board[i].get(j) for j in range(9)] for i in range(9)]
        # return [cell for sub_board in self.board for cell in sub_board]

    # OBSOLETE FUNCTION
    # def is_full(self):
    #     return all(cell != 0 for sub_board in self.board for cell in sub_board)
    
    def get_valid_moves(self):
        valid_moves = []

        for board_index in range(9):
            for cell_index in range(9):
                if self.is_valid_move(board_index, cell_index):
                    valid_moves.append(board_index * 9 + cell_index)
        
        return valid_moves

        # OBSOLETE CODE
        # for board_index in range(9):
        #     if self.main_board[board_index] == 0:
        #         for cell_index in range(9):
        #             if self.board[board_index][cell_index] == 0:
        #                 valid_moves.append(board_index * 9 + cell_index)
        # return valid_moves

class TicTacToeNN(nn.Module):
    def __init__(self):
        super(TicTacToeNN, self).__init__()
        self.fc1 = nn.Linear(81, 128)
        self.fc2 = nn.Linear(128, 128)
        self.fc3 = nn.Linear(128, 128)
        self.fc4 = nn.Linear(128, 128)
        self.fc5 = nn.Linear(128, 81)  # 81 possible moves

    def forward(self, x):
        x = torch.flatten(x, start_dim=1)
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = torch.relu(self.fc3(x))
        x = torch.relu(self.fc4(x))
        x = self.fc5(x)
        return x

model = TicTacToeNN()
optimizer = optim.Adam(model.parameters(), lr=0.2)
criterion = nn.MSELoss()

class Agent:
    def __init__(self, model):
        self.model = model
        self.epsilon = 0.2 # Exploration factor

    def select_action(self, state, valid_moves):
        if len(valid_moves) == 0:
            return None # No valid moves left

        if np.random.rand() < self.epsilon:
            return np.random.choice(valid_moves) # Random valid action (exploration)
        else:
            state_tensor = torch.tensor(state, dtype=torch.float32).unsqueeze(0)
            with torch.no_grad():
                q_values = self.model(state_tensor).squeeze()
            # Mask invalid moves
            mask = torch.zeros(81, dtype=torch.bool)
            mask[valid_moves] = 1
            q_values[~mask] = -float('inf')
            return torch.argmax(q_values).item()

    def train(self, replay_buffer, batch_size=64):
        if len(replay_buffer) < batch_size:
            return

        batch = random.sample(replay_buffer, batch_size)
        states, actions, rewards, next_states, dones = zip(*batch)

        states_tensor = torch.tensor(states, dtype=torch.float32)
        actions_tensor = torch.tensor(actions, dtype=torch.int64)
        rewards_tensor = torch.tensor(rewards, dtype=torch.float32)
        next_states_tensor = torch.tensor(next_states, dtype=torch.float32)
        dones_tensor = torch.tensor(dones, dtype=torch.float32)

        q_values = self.model(states_tensor).gather(1, actions_tensor.unsqueeze(1)).squeeze()
        next_q_values = self.model(next_states_tensor).max(1)[0]
        target_q_values = rewards_tensor + (1 - dones_tensor) * 0.9 * next_q_values

        loss = criterion(q_values, target_q_values)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

def play_game(agent, game, replay_buffer):
    game.reset()
    state = game.get_state()
    while game.check_winner() == 0:
        valid_moves = game.get_valid_moves()
        action = agent.select_action(state, valid_moves)
        if action is None: # No valid moves left
            break
        board_index, cell_index = divmod(action, 9)
        if game.make_move(board_index, cell_index):
            next_state = game.get_state()
            reward = 9999999999 if game.check_winner() == game.current_player else 0
            reward = -9999999999 if game.check_winner() == 3 - game.current_player else 0
            if game.main_board[board_index].won_by == game.current_player:
                reward += 100
            elif game.main_board[board_index].won_by == 3 - game.current_player:
                reward -= 100
            replay_buffer.append((state, action, reward, next_state, game.check_winner() != 0))
            state = next_state
        else:
            reward = -999999999 # Penalty for invalid move
            replay_buffer.append((state, action, reward, state, False))

    agent.train(replay_buffer)

def save_model(model, filepath):
    torch.save(model.state_dict(), filepath)

def load_model(filepath):
    model = TicTacToeNN()
    model.load_state_dict(torch.load(filepath))
    model.eval()
    return model

def train_agent():
    game = UltimateTicTacToe()
    model = TicTacToeNN()
    agent = Agent(model)
    replay_buffer = []

    for episode in range(200000):
        play_game(agent, game, replay_buffer)
        if episode % 100 == 0:
            print(f"Episode {episode} completed")

        # Optionally save the model at regular intervals
        if episode % 10000 == 0:
            save_model(model, f"tic_tac_toe_model_{episode}.pth")

    # Save the final model
    save_model(model, "tic_tac_toe_model_final.pth")

if __name__ == "__main__":
    train_agent()