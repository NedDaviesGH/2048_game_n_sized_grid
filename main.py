from fasthtml.common import *
from game import Game
from config import GameConfig

app = FastHTML(exts='ws')
rt = app.route

# Define a default color for tiles
default_tile_color = '#ccc'

# Example tile color dictionary
tile_colour_dict = {
    2: '#eee4da',
    4: '#ede0c8',
    8: '#f2b179',
    16: '#f59563',
    32: '#f67c5f',
    64: '#f65e3b',
    128: '#edcf72',
    256: '#edcc61',
    512: '#edc850',
    1024: '#edc53f',
    2048: '#edc22e',
    None: default_tile_color  # Default color for empty tiles
}

# Global variables to store the game and config
game = None
config = None

@rt('/')
def choose_size():
    return Html(
        Head(
            Title("Choose Grid Size"),
            Link(rel="icon", href="data:image/svg+xml;charset=UTF-8,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'><rect width='32' height='32' fill='%23FFA500'/></svg>"),
            Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css"),
            Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"),
            Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.9.3/css/bulma.min.css"),
            Style("""
                body {
                    background-color: #808080;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
                .container {
                    text-align: center;
                }
                .buttons {
                    display: flex;
                    justify-content: center;
                    flex-wrap: wrap;
                }
                .button {
                    margin: 5px;
                    font-size: 24px;
                    color: white;
                    background-color: black;
                    text-align: center;
                    text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff;
                }
            """)
        ),
        Body(
            Div(cls='container')(
                H1("Choose Grid Size", cls='title has-text-centered'),
                Div(cls='buttons')(
                    *[Button(str(size), cls='button', onclick=f"startGame({size})") for size in range(4, 13)]
                ),
                Script("""
                    function startGame(size) {
                        fetch('/start', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({ size: size })
                        }).then(response => response.json()).then(data => {
                            if (data.success) {
                                window.location.href = '/game';
                            }
                        });
                    }
                """)
            )
        )
    )
@rt('/start', methods=['POST'])
async def start(request):
    data = await request.json()
    size = data['size']
    global game, config
    config = GameConfig(background='#808080', size=size)
    game = Game(config.size)
    game.start_game()
    return {'success': True}

@rt('/game')
def game_page():
    global game, config
    if game is None:
        return Html(
            Head(
                Title("Error"),
                Link(rel="icon", href="data:image/svg+xml;charset=UTF-8,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'><rect width='32' height='32' fill='%23FFA500'/></svg>"),
                Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css"),
                Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"),
                Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.9.3/css/bulma.min.css"),
                Style("""
                    body {
                        background-color: #808080;
                        display: flex;
                        justify-content: center;
                        align-items: center;
                        height: 100vh;
                        margin: 0;
                    }
                    .container {
                        text-align: center;
                    }
                    .button {
                        margin: 5px;
                        font-size: 24px;
                        color: black;
                        text-align: center;
                        font-weight: bold;
                        text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff;
                    }
                """)
            ),
            Body(
                Div(cls='container')(
                    H1("Error: Game not initialized", cls='title has-text-centered'),
                    Button("Go Back", cls='button is-primary', onclick="window.location.href='/'")
                )
            )
        )
    board = game.get_board()
    return Html(
        Head(
            Title("2ned48"),
            Link(rel="icon", href="data:image/svg+xml;charset=UTF-8,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'><rect width='32' height='32' fill='%23FFA500'/></svg>"),
            Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css"),
            Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"),
            Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.9.3/css/bulma.min.css"),
            Style(f"""
                body {{
                    background-color: #808080;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }}
                .board {{
                    display: grid;
                    grid-template-columns: repeat({config.size}, 1fr);
                    gap: 10px;
                }}
                .tile {{
                    width: 100px;
                    height: 100px;
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    font-size: 24px;
                    border-radius: 15px;
                    background-color: #ccc;
                    color: black;
                    text-align: center;
                    font-weight: bold;
                    position: relative;
                }}
                .tile::before {{
                    content: attr(data-value);
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    color: white;
                    font-size: 24px;
                    font-weight: bold;
                    text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000;
                }}
                .new-tile {{
                    animation: fade-in 0.5s ease;
                }}
                @keyframes fade-in {{
                    0% {{
                        background-color: yellow;
                    }}
                    100% {{
                        background-color: #eee4da; /* Color for tile with value 2 */
                    }}
                }}
                .game-over {{
                    position: absolute;
                    top: 50%;
                    left: 50%;
                    transform: translate(-50%, -50%);
                    background-color: rgba(0, 0, 0, 0.8);
                    color: white;
                    padding: 20px;
                    border-radius: 10px;
                    text-align: center;
                }}
                .button {{
                    margin: 5px;
                    font-size: 24px;
                    color: black;
                    text-align: center;
                    font-weight: bold;
                    text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff;
                }}
            """)
        ),
        Body(
            Div(cls='board')(
                *[Div(cls=f'tile { "new-tile" if tile.new else "" }', style=f'background-color: {tile_colour_dict.get(tile.value, default_tile_color)};', data_value=str(tile.value) if tile.value else '')(
                    str(tile.value) if tile.value else ''
                ) for row in board for tile in row]
            ),
            Div(id='game-over', cls='game-over', style='display: none;')(
                H1("Game Over"),
                Button("Restart", cls='button', onclick="window.location.href='/'")
            ),
            Button("Restart", cls='button', onclick="window.location.href='/'"),
            Script("""
                document.addEventListener('keydown', function(event) {
                    let direction;
                    switch(event.key) {
                        case 'ArrowUp':
                            direction = 'up';
                            break;
                        case 'ArrowDown':
                            direction = 'down';
                            break;
                        case 'ArrowLeft':
                            direction = 'left';
                            break;
                        case 'ArrowRight':
                            direction = 'right';
                            break;
                        default:
                            return;
                    }
                    fetch('/move', {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                        body: JSON.stringify({ direction: direction })
                    }).then(response => response.json()).then(data => {
                        if (data.running === false) {
                            document.getElementById('game-over').style.display = 'block';
                        } else {
                            location.reload();
                        }
                    });
                });

                let touchstartX = 0;
                let touchstartY = 0;
                let touchendX = 0;
                let touchendY = 0;

                function handleGesture() {
                    let direction;
                    if (touchendX < touchstartX) direction = 'left';
                    if (touchendX > touchstartX) direction = 'right';
                    if (touchendY < touchstartY) direction = 'up';
                    if (touchendY > touchstartY) direction = 'down';
                    if (direction) {
                        fetch('/move', {
                            method: 'POST',
                            headers: {
                                'Content-Type': 'application/json'
                            },
                            body: JSON.stringify({ direction: direction })
                        }).then(response => response.json()).then(data => {
                            if (data.running === false) {
                                document.getElementById('game-over').style.display = 'block';
                            } else {
                                location.reload();
                            }
                        });
                    }
                }

                document.addEventListener('touchstart', function(event) {
                    touchstartX = event.changedTouches[0].screenX;
                    touchstartY = event.changedTouches[0].screenY;
                }, false);

                document.addEventListener('touchend', function(event) {
                    touchendX = event.changedTouches[0].screenX;
                    touchendY = event.changedTouches[0].screenY;
                    handleGesture();
                }, false);
            """)
        )
    )

@rt('/move', methods=['POST'])
async def move(request):
    data = await request.json()
    direction = data['direction']
    game.play_game(direction=direction)
    if game.check_loss_condition():
        game.end_game()
        return {'running': False}
    return {'running': True}

serve()