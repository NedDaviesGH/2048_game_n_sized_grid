from fasthtml.common import *
from backend.components.sidebar import Sidebar

def BaseLayout(title, content):
    return Html(
        Head(
            Title(title),
            Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.min.css"),
            Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css"),
            Link(rel="stylesheet", href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.9.3/css/bulma.min.css"),
            Link(rel="stylesheet", href="https://fonts.googleapis.com/css2?family=Lato:ital,wght@0,100;0,300;0,400;0,700;0,900;1,100;1,300;1,400;1,700;1,900&display=swap"),            
            Link(rel="stylesheet", href="/css/components/sidebar.css"),  # Include your custom sidebar styles,
            Link(rel="stylesheet", href="/css/components/content-wrapper.css"),
            Link(rel="stylesheet", href="/css/game/game.css"),  # Include game.css globally
            Link(rel="stylesheet", href="/css/theme/fonts.css"),

        ),
        Body(cls="is-family-primary")(
            Div(cls="columns is-gapless")(
                Div(cls="column is-1")(
                    Sidebar()  # Include the sidebar on every page
                ),
                Div(cls="column has-background-white-ter ")(
                    Div(cls="justify-content-center")(
                        Div(cls="content-wrapper")(
                            content  # Dynamic content for each page
                        )
                    )
                )
            )
        )
    )