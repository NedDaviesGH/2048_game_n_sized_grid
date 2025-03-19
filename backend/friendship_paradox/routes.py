from fasthtml.common import *
from backend.components.sidebar import Sidebar
from backend.components.layout import BaseLayout
from .logic.friends import make_friends, analyse_friends

def register_friends_routes(app):
    rt = app.route

    @rt('/friends', methods=['GET', 'POST'])
    async def friends_page(request):
        person_mean = None
        friend_mean = None
        num_friends = None
        is_normal = None

        if request.method == 'POST':
            # Get form data
            form_data = await request.form()
            num_friends = int(form_data.get('num_friends', 0))
            is_normal = form_data.get('is_normal', 'false') == 'true'

            # Generate friends and analyze
            friends = make_friends(num_friends, is_normal)
            person_mean, friend_mean = analyse_friends(friends)

        content = Html(
            Head(
                Title("Friendship Paradox"),
                Link(rel="icon", href="data:image/svg+xml;charset=UTF-8,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'><rect width='32' height='32' fill='%23FFA500'/></svg>"),
                # Link(rel="stylesheet", href="/css/components/sidebar.css"),
            ),
            Body(
                Div(cls='container')(
                    
                    H1("Friendship Paradox", cls='title has-text-centered'),
                    Div(cls='content')(
                        H2("Demonstration of the friendship paradox i.e. your friends are more likely to have more friends than you", cls='subtitle'),
                        P(f"Notice that you get very different results depending on what distribution you choose...")
                    ),
                    Form(action="/friends", method="POST", cls='form')(
                        Div(cls='field')(
                            Label("Number of Friends:", cls='label'),
                            Div(cls='control')(
                                Input(type="number", name="num_friends", cls='input', required=True, min=1)
                            )
                        ),
                        Div(cls='field')(
                            Label("Normal Distribution:", cls='label'),
                            Div(cls='control')(
                                Label(cls='checkbox')(
                                    Input(type="checkbox", name="is_normal", value="true"),
                                    " Enable Normal Distribution"
                                )
                            )
                        ),
                        Div(cls='field')(
                            Div(cls='control')(
                                Button("Analyze", type="submit", cls='button is-primary')
                            )
                        )
                    ),
                    Button("Back", cls="button is-danger", onclick="window.location.href='/'"),
                    # Display results if available
                    Div(cls='content')(
                        H2("Results", cls='subtitle') if person_mean is not None else '',
                        P(f"Number of Friends: {num_friends}") if num_friends is not None else '',
                        P(f"Normal Distribution: {'Yes' if is_normal else 'No'}") if is_normal is not None else '',
                        P(f"Your number of friends: {person_mean:.2f}") if person_mean is not None else '',
                        P(f"The average friend's number of friends: {friend_mean:.2f}") if friend_mean is not None else ''
                    )
                )
            )
        )
        
        return BaseLayout("Friends", content)