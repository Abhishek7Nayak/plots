import pandas as pd
import plotly.graph_objects as go

# Read the CSV data
df = pd.read_csv("/home/abhisab1/ITP/sankey/itp_sankey_data.csv")

# Define the node positions and colors
node_positions = [0.5, 0.95, 0.5, 0.95, 0.001, 0.5, 0.95, 0.001, 0.001, 0.001, 0.001, 0.5, 0.95, 0.5, 0.95]
node_colors = ['#e6e6fa', '#e6e6fa', '#F8961E', '#F8961E', '#43AA8B', '#85429b', '#85429b', '#666666', '#666666', '#666666', '#577590', '#577590', '#577590', '#440033', '#440033']

# Filter the data based on the "line" column
df['line'] = df['line'].astype(int)
df = df[df["line"] < 3]

# Create a sorted list of unique nodes
nodes = sorted(set(df["source"]) | set(df["target"]))

# Create a dictionary to map nodes to indices
node_indices = {node: index for index, node in enumerate(nodes)}

# Map the source and target nodes to their respective indices
source_indices = [node_indices[x] for x in df["source"]]
target_indices = [node_indices[x] for x in df["target"]]

# Create the Sankey diagram
fig = go.Figure(data=[go.Sankey(
    arrangement='snap',
    node=dict(
        label=nodes,
        color=node_colors,
        pad=10,
        x=node_positions,
        y=[0.1] * len(nodes)
    ),
    link=dict(
        source=source_indices,
        target=target_indices,
        value=df["value"],
    )
)])

# Set the title and font size
fig.update_layout(title_text="ITP Line of Therapy", font_size=10)

# Display the figure
fig.show()
