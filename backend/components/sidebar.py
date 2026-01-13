from fasthtml.common import *

def Sidebar():
    return Div(cls="has-background-dark has-text-white has-text-weight-bold")(
        Aside(cls="menu")(
            P("Menu", cls="menu-label has-text-white is-1 has-text-weight-bold has-text-centered is-size-4"),
            Ul(cls="menu-list")(
                Li(A("Home", href="/", cls="has-text-white")),
                Li(A("Profile", href="/profile", cls="has-text-white"))
            ),
            P("Random", cls="menu-label has-text-white has-text-weight-bold"),
            Ul(cls="menu-list")(
                Li(A("Relaxation Gallery", href="/relaxation", cls="has-text-white"))
            ),
            P("Games", cls="menu-label has-text-white has-text-weight-bold"),
            Ul(cls="menu-list")(
                Li(A("2048 Game", href="/choose_size", cls="has-text-white"))
            ),
            P("Data/Computer Science", cls="menu-label has-text-white has-text-weight-bold"),
            Ul(cls="menu-list")(
                Li(A("Friendship Paradox", href="/friends", cls="has-text-white")),
                Li(A("Binary Search Tree", href="/binary-search-tree", cls="has-text-white"))
            )
        )
    )