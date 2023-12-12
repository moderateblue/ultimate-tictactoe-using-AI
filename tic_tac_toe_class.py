class TicTacToe():
    def __init__(self, position):
        self.position = position
		# 0 = nobody
		#'X'
		#'O'
		#'-' = tie
        self.won_by = 0
        self.board = [' ', ' ', ' ',
                      ' ', ' ', ' ',
                      ' ', ' ', ' ']

    def get(self, pos):
        return self.board[pos]

    def change(self, pos, to):
        if to == True:
            self.board[pos] = 'X'
        else:
            self.board[pos] = 'O'
	
    def check_small_win(self, winner):
        if winner:
            winner = 'X'
        else:
            winner = 'O'
		
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
                if (self.board[i] != ' '):
                    full = True
                else:
                    full = False
                    break
            if (full):
                self.won_by = '-'