import numpy as np
import plotly.graph_objects as go



class Node():
    def __init__(self, data, level=1):
        self.input_data = list(set(data))
        self.level = level
        self.value = self.pick_middle_value(self.input_data)
        self.left_data, self.right_data = self.split_data(self.remove_value_from_arr(self.input_data))
        if self.left_data:
            self.left = Node(self.left_data, level + 1)
        else:
            self.left = None
        if self.right_data:
            self.right = Node(self.right_data, level + 1)
        else:
            self.right = None

    def remove_value_from_arr(self, arr_list):
        return [x for x in arr_list if x != self.value]
        
    def pick_middle_value(self, arr_list):
        arr = np.array(arr_list)
        sorted_arr = np.sort(arr)
        median_index = len(arr) // 2
        return sorted_arr[median_index]
    
    def split_data(self, arr_list):
        arr = np.array(arr_list)
        left, right = arr[arr < self.value], arr[arr > self.value]
        return list(left), list(right)

    def print_tree(self, branch=''):
        indent = "  " * self.level 
        print(f"{indent}{branch}: {self.value}")
        if self.left:
            self.left.print_tree(branch='left')
        if self.right:
            self.right.print_tree(branch='right')

    def visualize_tree(self):
        nodes = []
        edges = []

        def traverse(node, parent=None):
            if node is None:
                return
            # Add the current node
            nodes.append((node.value, node.level))
            # Add edges to children
            if parent is not None:
                edges.append((parent.value, node.value))
            # Traverse left and right children
            traverse(node.left, node)
            traverse(node.right, node)

        # Start traversal from the root
        traverse(self)

        # Create a mapping of node values to their levels
        value_to_level = {value: level for value, level in nodes}

        # Extract x, y positions for nodes
        x = []
        y = []
        labels = []
        for value, level in nodes:
            x.append(value)
            y.append(-level)  # Negative level for downward tree
            labels.append(str(value))

        # Create edges for visualization
        edge_x = []
        edge_y = []
        for parent, child in edges:
            edge_x.extend([parent, child, None])
            edge_y.extend([-value_to_level[parent], -value_to_level[child], None])

        # Create the figure
        fig = go.Figure()

        # Add edges
        fig.add_trace(go.Scatter(
            x=edge_x,
            y=edge_y,
            mode='lines',
            line=dict(color='gray', width=1),
            hoverinfo='none'
        ))

        # Add nodes
        fig.add_trace(go.Scatter(
            x=x,
            y=y,
            mode='markers+text',
            marker=dict(size=10, color='blue'),
            text=labels,
            textposition='top center'
        ))

        # Update layout
        fig.update_layout(
            title="Binary Search Tree Visualization",
            showlegend=False,
            xaxis=dict(showgrid=False, zeroline=False),
            yaxis=dict(showgrid=False, zeroline=False),
            plot_bgcolor='white'
        )

        return fig