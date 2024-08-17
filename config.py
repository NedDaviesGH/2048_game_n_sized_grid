class GameConfig():
    def __init__(self, background, size):
        self.size = size
        self.multiplier = 2
        self.cube_dim = 800 / (self.multiplier * self.size)
        self.screen_width = 800
        self.screen_height = self.screen_width * 0.75
        self.background = background


RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
GRAY = (150, 150, 150)
WHITE = (255, 255, 255)
CREAM = (200, 200, 200)

tile_values = [2 ** n for n in range(10)]
tile_colours = [(255, 255 - (n * 20), 0 + (n * 20)) for n in range(10)]

tile_colour_dict = dict(zip(tile_values, tile_colours))