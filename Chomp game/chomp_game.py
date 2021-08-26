import pygame
from board import *
from player import *
from GUI import *

BOARD_SIZE_LIMIT = 50
CELL_SIZE = 40
MARGIN = 5

WIN = 0
LOSE = 1
CLICK_POISON = 2

""" Define colors """
RED = (204, 0, 0)
BROWN = (102, 51, 0)
GRAY = (216, 216, 205)
DARK_GRAY = (188, 183, 162)

class Game:
    def __init__(self, size, poison_location):
        self.size = size
        self.board = Board(size, poison_location)

        self.human_player = Human()
        self.ai_player = AI()
        self.ai_player.read_p_positions(poison_location)

        self.game_over = False

    def play(self):
        pygame.init()

        window_size_x = int((CELL_SIZE + MARGIN) * self.size + MARGIN)
        window_size_y = int((CELL_SIZE + MARGIN) * 3 + MARGIN)
        self.screen = pygame.display.set_mode([window_size_x, window_size_y])
        self.screen.fill(GRAY)

        pygame.display.set_caption("Chomp Game")
        self.draw_board()

        clock = pygame.time.Clock()
 
        while not self.game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.game_over = True

            self.step(self.human_player)

            if not self.game_over:
                pygame.time.wait(700)
                self.step(self.ai_player)

            clock.tick(60)

        pygame.time.wait(1400)
        pygame.quit()
	
    def step(self, player):
        if isinstance(player, Human):
            user_clicked = False
            
            while not user_clicked:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()

                        # Change the x/y screen coordinates to board coordinates
                        col = pos[0] // (CELL_SIZE + MARGIN)
                        row = pos[1] // (CELL_SIZE + MARGIN)

                        if self.board.is_poison(row, col):
                            self.game_over = True
                            self.end = CLICK_POISON
                            ### print("you lose, can't cleek on poisn")
                            return
                        if player.move(self.board, row, col):
                            user_clicked = True

        else: #player is AI
            player.move(self.board)
            
        self.draw_board()
        
        result = player.is_finished(self.board)
        self.game_over = result[0]
        self.end = result[1]

    def draw_board(self):
        board_mat = self.board.get_board()
        for row in range(3):
            for col in range(self.size):
                if board_mat[row, col] == 1:
                    color = BROWN
                elif board_mat[row, col] == 0:
                    color = DARK_GRAY
                elif board_mat[row, col] == -1:
                    color = RED
                else:
                    color = BROWN
                pygame.draw.circle(self.screen, color, [(MARGIN + CELL_SIZE) * col + MARGIN + CELL_SIZE / 2,
                                                        (MARGIN + CELL_SIZE) * row + MARGIN + CELL_SIZE / 2], CELL_SIZE / 2)
        pygame.display.flip()

    def get_end(self):
        return self.end


if __name__ == "__main__":
    
    start_window()

    game = Game(get_size(), get_poison_location())
    game.play()

    end = game.get_end()
    if end == WIN:
            win_window()
    elif end == LOSE:
        lose_window()
    elif end == CLICK_POISON:
        lose_window(True)
        
    

