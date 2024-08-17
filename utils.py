from pygame.locals import *


def draw_text(text, pos, colour, font, screen):
    img = font.render(text, True, colour)
    screen.blit(img, pos)


def get_key_press(event):
    running = True
    if event.key == K_ESCAPE:
        running = False
    elif event.key == K_UP:
        direction = 'up'
    elif event.key == K_DOWN:
        direction = 'down'    
    elif event.key == K_LEFT:
        direction = 'left'
    elif event.key == K_RIGHT:
        direction = 'right'    
    return direction, running     