import random
import json
from fasthtml.common import *
from backend.components.layout import BaseLayout
from .logic.node import Node
from .logic.search_tree import benchmark_search, aggregate_results, lookup_tree_value
from .logic.plot_results import plot_scatter_with_filter, simple_scatter_plot
from fh_plotly import plotly2fasthtml

def register_binary_search_tree_routes(app):
    rt = app.route

    @rt('/binary-search-tree', methods=['GET', 'POST'])
    async def home_page(request):
        random_numbers = None
        tree = None
        tree_plot_html = None
        benchmark_plot_html = None
        search_result = None
        num_to_generate = 20  # Default value for the slider

        if request.method == 'POST':
            form_data = await request.form()

            # Check if the "Create Data" button was clicked
            if "num_to_generate" in form_data:
                num_to_generate = int(form_data.get('num_to_generate', 20))
                random_numbers = [random.randint(1, 100) for _ in range(num_to_generate)]

            # Check if the "Generate List and Tree" button was clicked
            elif "generate_tree" in form_data:
                # Retrieve the random numbers from the hidden input field
                random_numbers = json.loads(form_data.get('random_numbers', '[]'))
                tree = Node(random_numbers)
                # Generate the Plotly figure and convert it to HTML
                tree_plot_html = tree.visualize_tree()

            # Check if the "Search" button was clicked
            elif "search_number" in form_data:
                # Retrieve the tree and search number
                random_numbers = json.loads(form_data.get('random_numbers', '[]'))
                tree = Node(random_numbers)
                tree_plot_html = tree.visualize_tree()
                
                search_value = form_data.get('search_value', '')
                if search_value:
                    try:
                        search_value = int(search_value)
                        if search_value in random_numbers:
                            steps = lookup_tree_value(search_value, tree)
                            search_result = {
                                'found': True,
                                'value': search_value,
                                'steps': steps
                            }
                        else:
                            search_result = {
                                'found': False,
                                'value': search_value
                            }
                    except ValueError:
                        search_result = {
                            'error': 'Please enter a valid number'
                        }
            
            elif "benchmark_data_structures" in form_data:
                # Preserve the tree and random numbers
                random_numbers = json.loads(form_data.get('random_numbers', '[]'))
                tree = Node(random_numbers)
                tree_plot_html = tree.visualize_tree()
                
                # Run benchmarks for both storage types
                benchmark_search_node = benchmark_search(storage_type='node', num_data_points=500, min=1, max=3)
                benchmark_search_list = benchmark_search(storage_type='list', num_data_points=500, min=1, max=3)
            
                # Aggregate the results
                df = aggregate_results(benchmark_search_node, benchmark_search_list)
                df.to_csv('benchmark_results.csv', index=False)
                
                print("\n=== Benchmark Data ===")
                print(f"DataFrame shape: {df.shape}")
                print(f"Columns: {df.columns.tolist()}")
                print(f"First few rows:\n{df.head()}")

                # Generate the scatter plot with actual benchmark data
                benchmark_plot_html = plot_scatter_with_filter(
                    df, 
                    'size_tree', 'time_tree', 
                    'size_list', 'time_list', 
                    type_col='Type', 
                    title='Binary Search Tree vs List: Lookup Performance'
                )
                print(f"\nPlot HTML type: {type(benchmark_plot_html)}")
                print(f"Plot HTML generated: {benchmark_plot_html is not None}")

        content = Html(
            Head(
                Title("Binary Tree Search"),
                Script(src="https://cdn.plot.ly/plotly-latest.min.js"),
                Script("""
                    function updateSliderValue(value) {
                        document.getElementById('slider-value').innerText = value + " numbers";
                    }
                """),
                Style("""
                    .slider {
                        width: 100%;
                    }
                    .numbers-container {
                        display: flex;
                        flex-wrap: wrap;
                        gap: 10px;
                        justify-content: center;
                        margin-top: 20px;
                    }
                    .number-box {
                        background-color: #f5f5f5;
                        border: 1px solid #ddd;
                        border-radius: 5px;
                        padding: 10px 15px;
                        font-size: 1.2em;
                        font-weight: bold;
                        color: #333;
                        text-align: center;
                        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
                    }
                """)
            ),
            Body(
                Div(cls="container")(
                    Div(cls="main-content")(
                        H1("Binary Search Tree", cls="title is-1 has-text-centered"),
                        P("This page shows how a binary search tree is a more efficient data structure for lookups compared to a list.", cls="content"),
                        Form(action="/binary-search-tree", method="POST")(
                            Div(cls="field")(
                                Label("Select how many random numbers to generate:", cls="label"),
                                Div(cls="control")(
                                    Input(
                                        type="range",
                                        name="num_to_generate",
                                        cls="slider",
                                        min=10,
                                        max=100,
                                        value=num_to_generate,
                                        step=1,
                                        oninput="updateSliderValue(this.value)"
                                    ),
                                ),
                                P(f"{num_to_generate} numbers", id="slider-value", cls="help is-info")
                            ),
                            Button("Create Data", type="submit", cls="button is-primary")
                        ),
                        Div(cls="content")(
                            H2("Generated Numbers:", cls="subtitle") if random_numbers else '',
                            Div(cls="numbers-container")(
                                *[Div(str(num), cls="number-box") for num in random_numbers]
                            ) if random_numbers else ''
                        ),
                        Form(action="/binary-search-tree", method="POST")(
                            # Pass the random numbers as a hidden input field
                            Input(type="hidden", name="random_numbers", value=json.dumps(random_numbers)) if random_numbers else '',
                            Button("Generate List and Tree", type="submit", name="generate_tree", cls="button is-primary")
                        ) if random_numbers else '',
                        Div(cls="content")(
                            H2("Binary Search Tree:", cls="subtitle") if tree_plot_html else '',
                            Div(cls="plotly-container")(
                                plotly2fasthtml(tree_plot_html)
                            ) if tree_plot_html else ''
                        ),
                        Div(cls="content")(
                            H2("Search for a Number:", cls="subtitle") if tree_plot_html else '',
                            P("Enter a number to search for in the tree:", cls="content") if tree_plot_html else '',
                        ) if tree_plot_html else '',
                        Form(action="/binary-search-tree", method="POST")(
                            Input(type="hidden", name="random_numbers", value=json.dumps(random_numbers)) if random_numbers else '',
                            Div(cls="field has-addons")(
                                Div(cls="control is-expanded")(
                                    Input(
                                        type="number",
                                        name="search_value",
                                        cls="input",
                                        placeholder="Enter a number to search"
                                    )
                                ),  
                                Div(cls="control")(
                                    Button("Search", type="submit", name="search_number", cls="button is-info")
                                )
                            )
                        ) if tree_plot_html else '',
                        Div(cls="content")(
                            Div(cls="notification is-success" if search_result and search_result.get('found') else "notification is-warning" if search_result and not search_result.get('found') and not search_result.get('error') else "notification is-danger")(
                                P(f"✓ Found {search_result['value']} in {search_result['steps']} steps!", cls="content") if search_result and search_result.get('found') else
                                P(f"✗ {search_result['value']} is not in the tree.", cls="content") if search_result and not search_result.get('found') and not search_result.get('error') else
                                P(search_result.get('error', ''), cls="content") if search_result and search_result.get('error') else ''
                            )
                        ) if search_result else '',
                        Form(action="/binary-search-tree", method="POST")(
                            Input(type="hidden", name="random_numbers", value=json.dumps(random_numbers)) if random_numbers else '',
                            Button("Benchmark Data Structures", type="submit", name="benchmark_data_structures", cls="button is-primary")
                        ) if tree_plot_html else '',
                        (Div(cls="content")(
                            H2("Benchmark Results:", cls="subtitle"),
                            Div(cls="plotly-container")(
                                NotStr(benchmark_plot_html.to_html(include_plotlyjs='cdn', div_id="benchmark-plot", config={'responsive': True}))
                            )
                        ) if benchmark_plot_html else '')                       
                    )
                )
            )
        )

        return BaseLayout("Home", content)