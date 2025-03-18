from fasthtml.common import *
from backend.home.routes import register_home_routes
from backend.game_2048.routes import register_game_routes
from backend.friendship_paradox.routes import register_friends_routes

app = FastHTML(exts='ws', static_path='frontend/static')
app.static_route_exts(static_path='frontend/static/')

print(f"Serving static files from: {app.static_route}")

register_home_routes(app)
register_game_routes(app)
register_friends_routes(app)


serve()