import os

class Player:
    def is_finished(self, board):
        raise NotImplementedError("Should have implemented the is_finished function")
        
    def move(self, board, x=0, y=0):
        raise NotImplementedError("Should have implemented the move function")


class Human(Player):
    def move(self, board, i, j):
        make_move = board.is_legal_move(i, j)
        if make_move:
            print("human make move "+ str(i)+", "+str(j)) ###
            board.update(i, j)
        return make_move

    def is_finished(self, board):
        is_fin = board.is_final_state()
        if is_fin:
            print("you won")
        return is_fin


class AI(Player):
    def __init__(self):
        self.p_positions = []
    
    def read_p_positions(self, poison_location):
        x = str(poison_location)
        p_positions_file = 'data/p_positions_' + x + '.txt'
        
        if not os.path.exists(p_positions_file):
            raise Exception("missing data")
    
        with open(p_positions_file, 'r') as fhand:
            for line in fhand:
                p_position = line.split(',')
                if len(p_position) == 3:
                    p_position = [int(i) for i in p_position]
                    p_position = tuple(p_position)
                    self.p_positions.append(p_position)

        return self.p_positions
        
    def move(self, board):
        state = board.get_current_state()
        max_length = max(state)

        # Choose the optimal strategy, which ends the game most slow
        if state not in self.p_positions:
            for j in reversed(range(max_length)):
                for i in range(3):
                    if board.is_legal_move(i, j) and board.try_move(i, j) in self.p_positions:
                        print("ai make move "+ str(i)+", "+str(j)) ###
                        board.update(i, j)
                        return
            raise Exception("p position not found")
        else:
            for i in range(3):
                if board.is_legal_move(i, max_length-1):
                    board.update(i, max_length-1)
                    return

    def is_finished(self, board):
        is_fin = board.is_final_state()
        if is_fin:
            print("you lose")
        return is_fin
