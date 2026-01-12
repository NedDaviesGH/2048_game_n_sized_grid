from fasthtml.common import *
from backend.home.routes import register_home_routes
from backend.profile.routes import register_profile_routes
from backend.relaxation.routes import register_relaxation_routes
from backend.game_2048.routes import register_game_routes
from backend.friendship_paradox.routes import register_friends_routes
from backend.binary_search_tree.routes import register_binary_search_tree_routes
from fh_plotly import plotly_headers


app = FastHTML(exts='ws', static_path='frontend/static', hdrs=plotly_headers)
app.static_route_exts(static_path='frontend/static/')

print(f"Serving static files from: {app.static_route}")

register_home_routes(app)
register_profile_routes(app)
register_relaxation_routes(app)
register_game_routes(app)
register_friends_routes(app)
register_binary_search_tree_routes(app)


serve()