from board import Board

class Game:
    def __init__(self, size):
        self.board = Board(size)
        self.size = size

    def start_game(self):
        self.board.print_board()

    def get_board(self):
        return self.board.get_current_board()
    
    def play_game(self, direction):
        self.board.make_move(direction)
        self.board.fill_squares_and_check()
        self.board.print_board()


    def end_game(self):
        print('You lost buddy')
        


    def check_loss_condition(self):
        if self.board.grid_full == True:
            return True
        return False 





