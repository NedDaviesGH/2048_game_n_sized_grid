from fasthtml.common import *
from backend.components.layout import BaseLayout
import os

def register_relaxation_routes(app):
    rt = app.route

    @rt('/relaxation')
    def relaxation_page():
        # Path to the relaxation images directory
        pics_dir = 'frontend/static/pics/relaxation'
        # Get all .jpg files in the directory
        images = [img for img in os.listdir(pics_dir) if img.endswith('.jpg')]

        content = Html(
            Head(
                Title("Relaxation Gallery"),
                # Link(rel="stylesheet", href="/css/home/home.css"),
                # Link(rel="stylesheet", href="/css/components/sidebar.css"),
                Style("""
                    .gallery {
                        display: flex;
                        flex-wrap: wrap;
                        gap: 10px;
                        padding: 10px;
                        justify-content: center;
                    }
                    .gallery img {
                        max-height: 300px;
                        border-radius: 10px;
                        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
                    }
                """)
            ),
            Body(
                Div(cls="container")(
                    Div(cls="main-content")(
                        H1("Relaxation Gallery", cls="title is-1 has-text-centered"),
                        P("Scroll through the images below to relax."),
                        Div(cls="gallery")(
                            # Dynamically add images from the directory
                            *[Img(src=f"/pics/relaxation/{img}", alt=f"Image {i+1}") for i, img in enumerate(images)]
                        )
                    )
                )
            )
        )
        
        return BaseLayout("Relaxation Gallery", content) 