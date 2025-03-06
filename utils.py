def get_key_press(event):
    running = True
    direction_pressed = False
    direction = None
    if event == 'Escape':
        running = False
    elif event == 'ArrowUp':
        direction = 'up'
    elif event == 'ArrowDown':
        direction = 'down'
    elif event == 'ArrowLeft':
        direction = 'left'
    elif event == 'ArrowRight':
        direction = 'right'
    if direction:
        direction_pressed = True
    return direction_pressed, direction, running