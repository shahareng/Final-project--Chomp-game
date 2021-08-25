import numpy as np

class Board:
    """
    Use a 2d array to store board state
    ones for blocks, zeros for eaten blocks, and -1 for poison
    """
    def __init__(self, n, poison_location):
        self.width = n
        self.height = 3
        self.poison_location = poison_location
        
        self.current_state = [n, n, n] # first line, second and third
        self.final_state = []
        self.board = np.ones((self.height, self.width), dtype=np.int)

        if self.poison_location == 1:
            self.board[1][0] = -1
            self.board[2][0] = -1

            self.final_state = [1, 1, 0]
            
        elif self.poison_location == 2:
            self.board[1][0] = -1
            self.board[2][2] = -1 ### [2][0], [2][1] ?
            self.board[2][0] = 0
            self.board[2][1] = 0

            self.final_state = [3, 1, 0]
            
        elif self.poison_location == 3:
            self.board[0][0] = -1
            self.board[2][1] = -1 ### [1][0], [2][0] ?
            self.board[1][0] = 0
            self.board[2][0] = 0

            self.final_state = [2, 1, 1]
            
        elif self.poison_location == 4:
            self.board[2][0] = -1
            self.board[2][1] = -1

            self.final_state = [2, 0, 0]

    def is_legal_move(self, row, col):
        return self.board[row][col] == 1

    def is_poison(self, row, col):
        return self.board[row][col] == -1

    def update(self, row, col):
        for r in range(row+1):
            self.current_state[2 - r] = min(self.current_state[2 - r], col)
        for r in range(row+1):
            self.board[r][col:] = 0 # elements after index col

    def try_move(self, row, col):
        temp_state = self.current_state.copy()
        for r in range(row+1):
            temp_state[2 - r] = min(temp_state[2 - r], col)
        return tuple(temp_state)

    def is_final_state(self):
        return self.current_state == self.final_state

    def get_board(self):
        return self.board
            
    def get_current_state(self):
        return tuple(self.current_state)
        
