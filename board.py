import numpy as np
from tile import Tile

class Board:
    def __init__(self, size):
        self.size = size
        self.board = self.make_board(size)
        self.score = 0
        self.grid_full = False
        self.direction_mapping = {
            'down': 1,
            'left': 2, 
            'up': 3,
            'right': 4
        }


    def make_board(self, size):
        board = np.array([[Tile(value=None) for n in range(size)] for n in range(size)])
        board = self.populate_random_empty_tiles(board, start=True)
        return board
    

    def print_board(self):
        print('')
        print(np.array([[tile.value if isinstance(tile.value, int) else 'x' for tile in row] for row in self.board]))
        print('')



    def get_current_board(self):
        return self.board
    

    def pick_random_empty_tiles(self, board, num_tiles):
        # pick n random empty tiles
        empty_tiles_idxs = self.get_empty_tiles_idxs(board)

        n_random_empty_idxs = empty_tiles_idxs[np.random.choice(empty_tiles_idxs.shape[0], num_tiles, replace=False)]

        return n_random_empty_idxs
    

    def get_empty_tiles_idxs(self, board):
        empty_indices = np.array([index for index, tile in np.ndenumerate(board) if tile.value is None])
        return empty_indices


    def populate_random_empty_tiles(self, board, start=False):
        if start:
            num_tiles = 2
        else:
            num_tiles = np.random.randint(1,3)
        random_idxs = self.pick_random_empty_tiles(board, num_tiles=num_tiles)
        for tile_idx in random_idxs:
            board[tuple(tile_idx)].value = 2
            board[tuple(tile_idx)].new = True


        return board


    def make_move(self, direction):
        direction = self.direction_mapping[direction]
        board = self.board
        
        board_values = self.shift_board_tiles(
            self.board_tiles_to_values(board), 
            direction
        )
     

        board_values = self.combine_tiles(
            board_values, 
            direction
        )


        
        self.board = self.board_values_to_tiles(board, board_values)
        
        for row in board:
            for tile in row:
                tile.new = False

        print('you made a move')


    def fill_squares_and_check(self):
        print('filling empty squares with numbers')
        self.board = self.populate_random_empty_tiles(self.board)
        self.check_grid_full()


    def board_tiles_to_values(self, board):
        return np.array([[tile.value for tile in row] for row in board])
    

    def board_values_to_tiles(self, board, board_int):
        for i, row in enumerate(board):
            for j, tile in enumerate(row):
                tile.value = board_int[i, j]
        return board
    


    def shift_row_tiles(self, row):
        print('pre shifted row', row)
        row = row[row != np.array(None)]
        row = np.append([None for n in range(self.size - len(row))], row)
        print('post shifted row', row)
        print('')
        return row


    def shift_board_tiles(self, board, direction):
        # I think there is a problem in either this logic or the combine_tiles logic
        # rotate board accordingly: right = 0, up = 1, left = 2, down = 3
        board = np.rot90(board, direction)
        for row in range(len(board)):
            board[row] = self.shift_row_tiles(board[row])

        # reverse board rotation
        board = np.rot90(board, -direction)
        return board
    

    def check_any_adjacent_numbers_equal(self, row):
        for i in range(len(row) - 1):
            # print(f'{i}th element: {row[i]}', f'{i+1}th element: {row[i+1]}')
            if (row[i] == row[i + 1]) and (row[i] != None):
                # print('has adjacent numbers in row')
                return True
        return False



    def combine_tiles(self, board, direction):
        print('In combine_tiles_function')
        print(board)
        # I think there is a problem in either this logic or the shift_tiles logic
        # rotate board accordingly: right = 0, up = 1, left = 2, down = 3
        board = np.rot90(board, direction)
        # flipping board for ease in logic (looking backwards through numbers to check what to combine first)
        board_reversed = np.fliplr(board)
        for row in board_reversed:
            print(row)
            # only enter this nested loop if at least 2 adjacent elements are equal.
            if not self.check_any_adjacent_numbers_equal(row):
                print('could not find any adjacent numbers in row')
                continue

            
            for i in range(len(row) - 1):
                print(f'{i=}')
                if row[i] == None:
                    continue 
                if row[i] == row[i + 1]:
                    row[i] = row[i] * 2 
                    row[i + 1] = None
    
        # flip board back
        
        board = np.fliplr(board_reversed)
        
        # reverse board rotation
        board = np.rot90(board, -direction)
        # final shift for any new Nones introduced at merging step
        board = self.shift_board_tiles(board, direction)
        return board


    def calculate_score(self, tiles):
        pass


    def check_grid_full(self):
        board_values = self.board_tiles_to_values(self.board)
        if np.count_nonzero(board_values) == board_values.size:
            self.grid_full = True







