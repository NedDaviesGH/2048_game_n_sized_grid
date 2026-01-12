from fasthtml.common import *
from backend.components.layout import BaseLayout
from backend.components.sidebar import Sidebar  # Import the Sidebar component

def register_home_routes(app):
    rt = app.route
    @rt('/')
    def home_page():
        content = Html(
            Head(
                Title("Neddy"),
                # Link(rel="stylesheet", href="/css/home/home.css")  
            ),
            Body(
                Div(cls="container")(
                    Div(cls="main-content ")(
                        H1("Welcome", cls="title is-1 has-text-centered"),
                        P("This is a site for mini projects in data science, games, and my profile", cls="content")
                    )
                )
            )
        )
        
        return BaseLayout("Home", content)