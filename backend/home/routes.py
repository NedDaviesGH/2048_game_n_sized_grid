from fasthtml.common import *

def register_home_routes(app):
    rt = app.route
    @rt('/')
    def home_page():
        return Html(
            Head(
                Title("Home - 2048 Game"),
                Link(rel="stylesheet", href="/css/home/home.css")  
            ),
            Body(
                Div(cls="container")(
                    Div(cls="sidebar")(
                        H2("Menu"),
                        Button("2048 Game", cls="button", onclick="window.location.href='/choose_size'"),
                        Button("Friendship Paradox", cls="button", onclick="window.location.href='/friends'")
                    ),
                    Div(cls="main-content")(
                        H1("Welcome"),
                        P("This is the home page. Use sidebar to for other pages")
                    )
                )
            )
        )