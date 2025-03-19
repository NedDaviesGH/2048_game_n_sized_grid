from fasthtml.common import *
from backend.components.sidebar import Sidebar
from backend.components.layout import BaseLayout
from .logic.game import Game
from .logic.config import GameConfig

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

def register_game_routes(app):
    rt = app.route
    @rt('/choose_size')
    def choose_size():
        content = Html(
            Head(
                Title("Choose Grid Size"),
                Link(rel="icon", href="data:image/svg+xml;charset=UTF-8,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'><rect width='32' height='32' fill='%23FFA500'/></svg>"),
            ),
            Body(cls = "body-game")(
                Div(cls='game-container')(
                    H1("NxN 2048", cls='title is-1'),
                    H1("Choose Grid Size", cls='title'),
                    Div(cls='buttons')(
                        *[Button(str(size), cls='button', onclick=f"startGame({size})") for size in range(4, 9)]
                    ),
                    Button("Back", cls="button is-danger", onclick="window.location.href='/'"),  # Back button
                    Script(src='/js/game/grid_size.js')
                )
            )
        )
        
        return BaseLayout("2048", content)
    
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
            content = Html(
                Head(
                    Title("Error"),
                    Link(rel="icon", href="data:image/svg+xml;charset=UTF-8,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'><rect width='32' height='32' fill='%23FFA500'/></svg>"),
                    Style(f"""
                        .board {{
                            display: grid;
                            grid-template-columns: repeat({config.size}, 1fr);
                            gap: 10px;
                        }}
                    """)
                ),
                Body(cls = "game-container")(
                    Div(cls='board')(
                        *[Div(cls=f'tile { "new-tile" if tile.new else "" }', style=f'background-color: {tile_colour_dict.get(tile.value, default_tile_color)};', data_value=str(tile.value) if tile.value else '')(
                            str(tile.value) if tile.value else ''
                        ) for row in board for tile in row]
                    ),
                    Div(id='game-over', cls='game-over', style='display: none;')(
                        H1("Game Over"),
                        Button("Restart", cls='button', onclick="window.location.href='/choose_size'")
                    ),
                    Button("Restart", cls='button', onclick="window.location.href='/choose_size'"),
                    Script(src='/js/game/game_page.js')
                )
            )
            return BaseLayout("2048", content) 
        board = game.get_board()
        content = Html(
            Head(
                Title("2ned48"),
                Link(rel="icon", href="data:image/svg+xml;charset=UTF-8,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'><rect width='32' height='32' fill='%23FFA500'/></svg>"),
                Style(f"""
                    .board {{
                        display: grid;
                        grid-template-columns: repeat({config.size}, 1fr);
                        gap: 10px;
                    }}
                """)
            ),
            Body(cls = "body-game")(
                Div(cls = "game-container")(
                Div(cls='board')(
                    *[Div(cls=f'tile { "new-tile" if tile.new else "" }', style=f'background-color: {tile_colour_dict.get(tile.value, default_tile_color)};', data_value=str(tile.value) if tile.value else '')(
                        str(tile.value) if tile.value else ''
                    ) for row in board for tile in row]
                ),
                Div(id='game-over', cls='game-over', style='display: none;')(
                    H1("Game Over"),
                    Button("Restart", cls='button', onclick="window.location.href='/choose_size'")
                ),
                Button("Restart", cls='button', onclick="window.location.href='/choose_size'"),
                Script(src='/js/game/game_page_movement.js')
            )
            )
        )
        return BaseLayout("2048", content)

    @rt('/move', methods=['POST'])
    async def move(request):
        data = await request.json()
        direction = data['direction']
        game.play_game(direction=direction)
        if game.check_loss_condition():
            game.end_game()
            return {'running': False}
        return {'running': True}