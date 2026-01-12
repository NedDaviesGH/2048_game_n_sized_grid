from fasthtml.common import *
from backend.components.layout import BaseLayout
from .logic.friends import make_friends, analyse_friends, plot_friend_matrix, plot_popularity_distribution


def register_friends_routes(app):
    rt = app.route

    @rt('/friends', methods=['GET', 'POST'])
    async def friends_page(request):
        person_mean = None
        friend_mean = None
        num_friends = None
        is_normal = None
        global popularity_scoress
        global friends 
        friends = None
        popularity_scores = None
        

        if request.method == 'POST':
            # Get form data
            form_data = await request.form()
            num_friends = int(form_data.get('num_friends', 0))
            is_normal = form_data.get('is_normal', 'false') == 'true'

            # Generate friends and analyze


            friends, popularity_scores = make_friends(num_friends, is_normal)
            person_mean, friend_mean = analyse_friends(friends, popularity_scores)

        content = Html(
            Head(
                Title("Friendship Paradox"),
                Link(rel="icon", href="data:image/svg+xml;charset=UTF-8,<svg xmlns='http://www.w3.org/2000/svg' width='32' height='32' viewBox='0 0 32 32'><rect width='32' height='32' fill='%23FFA500'/></svg>"),
            ),
            Body(
                Div(cls='container')(
                    H1("Friendship Paradox", cls='title has-text-centered'),
                    Div(cls='content')(
                        H2("Demonstration of the friendship paradox i.e. your average friend is likely to have more friends than you!", cls='subtitle'),
                        P("This situation seems very counter-intuitive. You may understandably expect there to be a symmetrical relationship between your number of friends, and your friend's number of friends - so how does this paradox come about?"),
                        P("Run a simulation below and inspect the results")
                    ),
                    Form(action="/friends", method="POST", cls='form')(
                        Div(cls='field')(
                            Label("Select the total number of people in a friendship network (max 300):", cls='label'),
                            Div(cls='control')(
                                Input(type="number", name="num_friends", cls='input', required=True, min=2, max=300)
                            )
                        ),
                        Div(cls='field')(
                            Div(cls='control')(
                                Label(cls='checkbox')(
                                    Input(type="checkbox", name="is_normal", value="true"),
                                    " Enable Popularity Score Normal Distribution"
                                )
                            )
                        ),
                        Div(cls='field')(
                            Div(cls='control')(
                                Button("Analyze", type="submit", cls='button is-primary')
                            )
                        )
                    ),
                    # Button("Back", cls="button is-danger", onclick="window.location.href='/'"),
                    # Display results if available
                    Div(cls='content')(
                        H2("Results", cls='subtitle') if person_mean is not None else '',
                        P(f"Number of Friends: {num_friends}") if num_friends is not None else '',
                        P(f"Normal Distribution: {'Yes' if is_normal else 'No'}") if is_normal is not None else '',
                        P(f"Your number of friends: {person_mean:.2f}") if person_mean is not None else '',
                        P(f"The average friend's number of friends: {friend_mean:.2f}") if friend_mean is not None else '',
                        H3("Okay so it looks like the average number of friends someone has is less than their average friend's number of friends?") if friend_mean is not None else '',
                        P("One way we can intuitively understand this is by imagining 1 million people. If there's someone in that group who has 700,000 friends, and another person who has only 1 friend - who do you think you are more likely to be friends with? You are more likely to be friends with the person who has more friends, and this is the reason we see the friendship paradox. In other words: people who have more friends are overrepresented in the friend network.") if friend_mean is not None else '',
                        P("The matrix plot below shows who is friends with who. A dark square represents two people who are friends with eachother. It encapsulates the entire potential network of friends.") if friends is not None else ' ',
                        Div(cls='content')(
                            Div(plot_friend_matrix(friends)) if friends is not None else ' ',
                            P("How have we decided how many friends each person gets? Each person is assigned a popularity score according probability distribution (either uniform of normal depending on the option picked).") if friends is not None else ' ',
                            P("The popularity score dictates how likely someone is to get a friend. For example, if there are 100 potential friends for 1 person who has a popularity score of 0.8, then their expected number of friends is 80. This distribution was created at random, with a mean of 0.5. It is a simplified representation of how popularity is distributed amongst a social network.") if friends is not None else ' ',
                            Div(plot_popularity_distribution(popularity_scores)) if friends is not None else ' '
                        )
                    )
                )
            )
        )
        
        return BaseLayout("Friends", content)