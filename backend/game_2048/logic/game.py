from .board import Board
import numpy as np

class Game:
    def __init__(self, size):
        self.board = Board(size)
        self.size = size

    def start_game(self):
        self.board.print_board()

    def get_board(self):
        return self.board.get_current_board()
    
    def play_game(self, direction):
        current_board_values = self.board.get_tile_values()
        print('CURRENT', current_board_values)
        self.board.make_move(direction)
        new_board_values = self.board.get_tile_values()
        print('NEW BOARD', new_board_values)
        boards_equal = np.array_equal(current_board_values, new_board_values)
        print('are boards equal?', boards_equal)
        if not boards_equal:
            self.board.fill_squares_and_check()
        # self.board.print_board()

    def end_game(self):
        print('You lost buddy')
        

    def check_loss_condition(self):
        return self.board.grid_full





