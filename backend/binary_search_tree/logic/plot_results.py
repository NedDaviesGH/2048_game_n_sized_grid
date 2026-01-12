import plotly.express as px
import pandas as pd
import numpy as np

import plotly.express as px
import pandas as pd
import numpy as np

def plot_scatter_with_filter(df, x_col_tree, y_col_tree, x_col_list, y_col_list, type_col='Type', title='Scatter Plot'):
    """
    Plots a scatter plot with filters to toggle between Tree, List, Both, and log-transformed x-axis.

    Parameters:
        df (pd.DataFrame): The input DataFrame.
        x_col_tree (str): Column name for the x-axis values for "Tree".
        y_col_tree (str): Column name for the y-axis values for "Tree".
        x_col_list (str): Column name for the x-axis values for "List".
        y_col_list (str): Column name for the y-axis values for "List".
        type_col (str): Name of the categorical column for coloring (default: 'Type').
        title (str): Title of the plot (default: 'Scatter Plot').

    Returns:
        fig: Returns the Plotly figure object.
    """
    # Prepare the data in a long format
    df_long = pd.DataFrame({
        'Size': df[x_col_tree].tolist() + df[x_col_list].tolist(),
        'Time (seconds)': df[y_col_tree].tolist() + df[y_col_list].tolist(),
        type_col: ['Binary Search Tree'] * len(df[x_col_tree]) + ['List'] * len(df[x_col_list])
    })
    
    # Remove zero and negative values (can't plot on log scale)
    df_long = df_long[df_long['Time (seconds)'] > 0].copy()
    
    # Save for debugging
    df_long.to_csv('df_long.csv', index=False)
    print(f"df_long shape: {df_long.shape}")
    print(f"df_long head:\n{df_long.head()}")

    # Create the scatter plot with Plotly
    fig = px.scatter(
        df_long,
        x='Size',
        y='Time (seconds)',
        color=type_col,
        title=title,
        labels={'Size': 'Data Structure Size', 'Time (seconds)': 'Lookup Time (seconds)'},
        opacity=0.8,
        log_x=True,
        log_y=True  # Add log scale for y-axis too since times are very small
    )
    
    # Update layout to ensure proper display
    fig.update_layout(
        height=600,
        showlegend=True,
        xaxis_title="Data Structure Size (log scale)",
        yaxis_title="Lookup Time in seconds (log scale)"
    )
    
    # Update traces to make points more visible
    fig.update_traces(marker=dict(size=8))
    
    print(f"Figure created with {len(fig.data)} traces")
    if len(fig.data) > 0:
        print(f"Trace 0 name: {fig.data[0].name}, points: {len(fig.data[0].x)}")
        print(f"Trace 0 x sample: {fig.data[0].x[:5]}")
        print(f"Trace 0 y sample: {fig.data[0].y[:5]}")
    if len(fig.data) > 1:
        print(f"Trace 1 name: {fig.data[1].name}, points: {len(fig.data[1].x)}")
        print(f"Trace 1 x sample: {fig.data[1].x[:5]}")
        print(f"Trace 1 y sample: {fig.data[1].y[:5]}")
    print(f"X range: {df_long['Size'].min()} to {df_long['Size'].max()}")
    print(f"Y range: {df_long['Time (seconds)'].min()} to {df_long['Time (seconds)'].max()}")

    # # Add filters for Tree/List and log size
    # fig.update_layout(
    #     updatemenus=[
    #         # Filter for Tree, List, or Both
    #         dict(
    #             buttons=[
    #                 dict(label="Both", method="update", args=[{"visible": [True, True]}, {"title": f"{title} (Tree and List)"}]),
    #                 dict(label="Tree", method="update", args=[{"visible": [True, False]}, {"title": f"{title} (Tree Only)"}]),
    #                 dict(label="List", method="update", args=[{"visible": [False, True]}, {"title": f"{title} (List Only)"}]),
    #             ],
    #             direction="down",
    #             showactive=True,
    #             x=0.1,  # Position of the dropdown
    #             y=1.15
    #         ),
    #         # Filter for linear or log size
    #         dict(
    #             buttons=[
    #                 dict(label="Linear Size", method="update", args=[{"x": [df_long['x']]}, {"title": f"{title} (Linear Size)"}]),
    #                 dict(label="Log Size", method="update", args=[{"x": [df_long['log_x']]}, {"title": f"{title} (Log Size)"}]),
    #             ],
    #             direction="down",
    #             showactive=True,
    #             x=0.3,  # Position of the dropdown
    #             y=1.15
    #         )
    #     ]
    # )

    # Show the plot
    return fig


import plotly.express as px
import pandas as pd

def simple_scatter_plot():
    # Create a simple DataFrame for testing
    data = {
        'x': [1, 2, 3, 4, 5],
        'y': [10, 20, 15, 25, 30],
        'Type': ['Tree', 'Tree', 'List', 'List', 'Tree']
    }
    df = pd.DataFrame(data)

    # Create a basic scatter plot
    fig = px.scatter(
        df,
        x='x',
        y='y',
        color='Type',  # Different colors for Tree and List
        title='Simple Scatter Plot',
        labels={'x': 'X-Axis', 'y': 'Y-Axis'}
    )

    # Return the figure
    return fig