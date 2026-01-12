from fasthtml.common import *
from backend.components.layout import BaseLayout

def register_profile_routes(app):
    rt = app.route
    
    @rt('/profile')
    def profile_page():
        content = Html(
            Head(
                Title("Profile - Neddy"),
                Link(rel="stylesheet", href="/css/profile/profile.css")
            ),
            Body(
                Div(cls="container")(
                    Div(cls="main-content")(
                        H1("Profile", cls="title is-1 has-text-centered"),
                        Div(cls="profile-content")(
                            Div(cls="profile-section")(
                                H2("About Me", cls="title is-3"),
                                P("Hi, I'm Ned", cls="subtitle is-4"),
                                P("Data Scientist specialising in fintech applications with expertise in building production-grade machine learning models and delivering data-driven insights that drive business outcomes.", cls="content")
                            ),
                            Div(cls="profile-section")(
                                H2("Expertise", cls="title is-3"),
                                P(Strong("Fintech & Financial Services: "), "Extensive experience developing ML solutions for financial applications including transaction analysis, affordability assessment, and forecasting financial behaviours.", cls="content"),
                                P(Strong("Machine Learning & AI: "), "Building and deploying predictive models, classification systems, and time series forecasting solutions. Experienced with both traditional ML and deep learning approaches.", cls="content"),
                                P(Strong("Cloud & Infrastructure: "), "End-to-end ML lifecycle management using cloud platforms, containerisation, and scalable deployment architectures.", cls="content"),
                                P(Strong("Full-Stack Development: "), "Creating data-driven applications from backend APIs to interactive frontends, bridging the gap between data science and production systems.", cls="content")
                            ),
                            Div(cls="profile-section")(
                                H2("Technologies", cls="title is-3"),
                                Div(cls="tech-categories")(
                                    Div(cls="tech-category")(
                                        P(Strong("Languages:"), cls="mb-2"),
                                        Div(cls="tags are-medium")(
                                            Span("Python", cls="tag is-link"),
                                            Span("SQL", cls="tag is-link"),
                                            Span("JavaScript", cls="tag is-link"),
                                            Span("TypeScript", cls="tag is-link")
                                        )
                                    ),
                                    Div(cls="tech-category")(
                                        P(Strong("ML & Data Science:"), cls="mb-2"),
                                        Div(cls="tags are-medium")(
                                            Span("PyTorch", cls="tag is-info"),
                                            Span("PySpark", cls="tag is-info"),
                                            Span("Scikit-learn", cls="tag is-info"),
                                            Span("Time Series Analysis", cls="tag is-info"),
                                            Span("Statistical Modelling", cls="tag is-info"),
                                            Span("Deep Learning", cls="tag is-info")
                                        )
                                    ),
                                    Div(cls="tech-category")(
                                        P(Strong("Cloud & Data Platforms:"), cls="mb-2"),
                                        Div(cls="tags are-medium")(
                                            Span("AWS SageMaker", cls="tag is-success"),
                                            Span("AWS Athena", cls="tag is-success"),
                                            Span("Snowflake", cls="tag is-success"),
                                            Span("Docker", cls="tag is-success"),
                                            Span("Git", cls="tag is-success"),
                                            Span("CI/CD", cls="tag is-success")
                                        )
                                    ),
                                    Div(cls="tech-category")(
                                        P(Strong("Web Development:"), cls="mb-2"),
                                        Div(cls="tags are-medium")(
                                            Span("React", cls="tag is-warning"),
                                            Span("FastHTML", cls="tag is-warning"),
                                            Span("REST APIs", cls="tag is-warning")
                                        )
                                    )
                                )
                            ),
                            Div(cls="profile-section")(
                                H2("Education", cls="title is-3"),
                                Ul(cls="content")(
                                    Li(Strong("MSc Data Science")(" - University of St. Andrews (ongoing)")),
                                    Li(Strong("MChem Chemistry (First Class)")(" - University of Oxford"))
                                )
                            ),
                            Div(cls="profile-section")(
                                H2("Connect", cls="title is-3"),
                                Div(cls="links-container")(
                                    A(
                                        Div(cls="link-card")(
                                            I(cls="fab fa-linkedin fa-3x"),
                                            P("LinkedIn", cls="link-title")
                                        ),
                                        href="https://www.linkedin.com/in/neddavies/",
                                        target="_blank",
                                        cls="link-wrapper"
                                    ),
                                    A(
                                        Div(cls="link-card")(
                                            I(cls="fab fa-github fa-3x"),
                                            P("GitHub", cls="link-title")
                                        ),
                                        href="https://github.com/NedDaviesGH",
                                        target="_blank",
                                        cls="link-wrapper"
                                    )
                                )
                            )
                        )
                    )
                )
            )
        )
        
        return BaseLayout("Profile", content)
