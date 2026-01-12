from fasthtml.common import *

def Sidebar():
    return Div(cls="has-background-dark has-text-white has-text-weight-bold")(
        Aside(cls="menu")(
            P("Menu", cls="menu-label has-text-white is-1 has-text-weight-bold has-text-centered is-size-4"),
            Ul(cls="menu-list")(
                Li(A("Home", href="/", cls="has-text-white")),
                Li(A("Profile", href="/profile", cls="has-text-white")),
                Li(A("Relaxation Gallery", href="/relaxation", cls="has-text-white")),
                Li(A("2048 Game", href="/choose_size", cls="has-text-white")),
                Li(A("Friendship Paradox", href="/friends", cls="has-text-white")),
                Li(A("Binary Search Tree", href="/binary-search-tree", cls="has-text-white"))
            )
        )
    )