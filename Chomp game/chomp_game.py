import pygame
from board import *
from player import *

BOARD_SIZE_LIMIT = 50
CELL_SIZE = 40
MARGIN = 5

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

            if not self.game_over: ### close window
                pygame.time.wait(500)
                self.step(self.ai_player)

            clock.tick(60) ###

        pygame.time.wait(2000)
        pygame.quit()
	
    def step(self, player):
        if isinstance(player, Human):
            user_clicked = False
            
            while not user_clicked:
                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        pos = pygame.mouse.get_pos()
                                     # Change the x/y screen coordinates to grid coordinates
                        col = pos[0] // (CELL_SIZE + MARGIN)
                        row = pos[1] // (CELL_SIZE + MARGIN)

                        if self.board.is_poison(row, col):
                            self.game_over = True
                            print("you lose, can't cleek on poisn")
                            return
                        if player.move(self.board, row, col):
                            user_clicked = True

        else: #player is AI
            player.move(self.board)
            
        self.draw_board()              
        self.game_over = player.is_finished(self.board)

    def draw_board(self):
        board_mat = self.board.get_board()
        for row in range(3):
            for col in range(self.size):
                if board_mat[row, col] == 1:
                    color = BROWN
                elif board_mat[row, col] == 0:
                    color = DARK_GRAY
                else:
                    color = RED
                pygame.draw.circle(self.screen, color, [(MARGIN + CELL_SIZE) * col + MARGIN + CELL_SIZE / 2,
                                                        (MARGIN + CELL_SIZE) * row + MARGIN + CELL_SIZE / 2], CELL_SIZE / 2)
        pygame.display.flip()


if __name__ == "__main__":
    
    size = int(input("Enter board size 3*n: "))
    if (size > BOARD_SIZE_LIMIT):
        raise Exception("")
    
    poison_location = int(input("Select poison location, options 1 to 4: "))
    if (poison_location < 1) and (poison_location > 4):
        raise Exception("")
    
    game = Game(size, poison_location)
    game.play()

