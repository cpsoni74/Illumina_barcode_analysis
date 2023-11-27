import pandas as pd
import networkx as nx
import matplotlib.pyplot as plt

# Sample DataFrame (replace this with your actual data)
data = {
    'Barcode': ['TAGGCCACGG', 'CCATCGGAGC', 'GGTCTAATTA', 'CCATGGGCGC', 'CGTAACAGTC', 'TAGACGAAGG'],
    'aaRS': ['LNV', 'HGT', 'AGL', 'TIR', 'ATL', 'LNV']
}

df = pd.DataFrame(data)

# Create a directed graph
G = nx.DiGraph()

# Add nodes (barcodes) to the graph
barcodes = df['Barcode'].tolist()
G.add_nodes_from(barcodes)

# Add edges (associations between barcodes and aaRS)
edges = [(row['Barcode'], row['aaRS']) for _, row in df.iterrows()]
G.add_edges_from(edges)

# Set node positions (optional)
pos = nx.spring_layout(G)

# Draw the network diagram with longer arrows
plt.figure(figsize=(10, 8))
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=8, font_color='black', font_weight='bold', edge_color='gray', width=1.5, connectionstyle="bar,fraction=0.5")

# Customize the plot
plt.title('Network Diagram of Barcodes and aaRS Associations')
plt.axis('off')

# Show the plot
plt.show()
