from game import Game
import pygame
from config import *
from pygame.locals import *
from utils import draw_text, get_key_press
pygame.init()

config = GameConfig(background = GRAY, size = 4)

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((config.screen_width, config.screen_height))

game = Game(config.size)
game.start_game()
running = True

rect = Rect(50, 60, 200, 80)
board = game.get_board()

font = pygame.font.Font(None, 24)

 

while running:
    for event in pygame.event.get():
        if event.type == KEYDOWN:
            direction, running = get_key_press(event)
            game.play_game(direction = direction)
            board = game.get_board()

        elif event.type == QUIT:
            print('QUITTING')
            running = False

    if game.check_loss_condition() == True:
        game.end_game() 
        running = False

    screen.fill(config.background)

    for x, row in enumerate(board):
        for y, tile in enumerate(row):
            top_left = (((config.multiplier - 1) * config.size * config.cube_dim)/2) + (y * config.cube_dim)
            bottom_right = 0.5 * (((config.multiplier - 1) * config.size * config.cube_dim)/2) + (x * config.cube_dim)
            tile_rect = Rect(
                top_left, 
                bottom_right,  
                config.cube_dim - 2, 
                config.cube_dim - 2
            )
            pygame.draw.rect(screen, BLACK, (top_left - 1,
                                             bottom_right - 1, 
                                             config.cube_dim / 1,
                                             config.cube_dim / 1)
                                             ,1)
            if tile.value != None:
                
                if tile.new == True:
                    pygame.draw.rect(screen, RED, tile_rect, border_radius=25)
                else:
                    pygame.draw.rect(screen, tile_colour_dict[tile.value], tile_rect, border_radius=15)
                draw_text(
                    text = str(tile.value), 
                    pos = tile_rect.center, 
                    colour = BLACK, 
                    font = font, 
                    screen = screen
                    )
    
    pygame.display.set_caption('2ned48')
    pygame.display.flip()
    pygame.time.delay(100)

pygame.quit()