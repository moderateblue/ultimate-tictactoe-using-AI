class TicTacToe():
    def __init__(self, position):
        self.position = position
		# 0 = nobody
		#'X'
		#'O'
		#'-' = tie
        self.won_by = 0
        self.board = [0, 0, 0,
                      0, 0, 0,
                      0, 0, 0]

    def get(self, pos):
        return self.board[pos]

    def change(self, pos, to):
        if to == 1:
            self.board[pos] = 1
        else:
            self.board[pos] = 2
	
    def check_small_win(self):
        for winner in range(1, 3):
		
            #rows
            for i in range(0, 9, 3):
                if (self.board[i] == winner) and (self.board[i + 1] == winner) and (self.board[i + 2] == winner):
                    self.won_by = winner

            #columns
            for i in range(3):
                if (self.board[i] == winner) and (self.board[i + 3] == winner) and (self.board[i + 6] == winner):
                    self.won_by = winner
        
            #top left to bottom right
            if (self.board[0] == winner) and (self.board[4] == winner) and (self.board[8] == winner):
                self.won_by = winner
            #top right to bottom left
            elif (self.board[2] == winner) and (self.board[4] == winner) and (self.board[6] == winner):
                self.won_by = winner

        else:
            full = False
            for i in range(9):
                if (self.board[i] != 0):
                    full = True
                else:
                    full = False
                    break
            if (full):
                self.won_by = 3