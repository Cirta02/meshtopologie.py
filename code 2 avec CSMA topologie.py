import matplotlib.pyplot as plt
import networkx as nx

# Create the graph
G = nx.DiGraph()

# Nodes
nodesA = [f"Node A{i}" for i in range(1, 6)]  # 5 nodes for group A
nodesBC = ["Node B", "Node C"]  # Nodes B and C

# Add nodes
G.add_node("Internet")
G.add_node("Router")
G.add_node("Switch A")
G.add_node("Switch BC")

for node in nodesA:
    G.add_node(node)

for node in nodesBC:
    G.add_node(node)

# Edges with attributes
G.add_edge("Internet", "Router", bandwidth="100 Mbps", delay="6560 ns")
G.add_edge("Router", "Switch A", bandwidth="100 Mbps", delay="6560 ns")
G.add_edge("Router", "Switch BC", bandwidth="100 Mbps", delay="6560 ns")

for node in nodesA:
    G.add_edge("Switch A", node, bandwidth="100 Mbps", delay="6560 ns")

for node in nodesBC:
    G.add_edge("Switch BC", node, bandwidth="100 Mbps", delay="6560 ns")

# Define positions for nodes
pos = {
    "Internet": (0, 0),
    "Router": (0, 1),
    "Switch A": (-1, 2),
    "Switch BC": (1, 2),
    nodesA[0]: (-1.5, 3),
    nodesA[1]: (-1, 3),
    nodesA[2]: (-0.5, 3),
    nodesA[3]: (0, 3),
    nodesA[4]: (0.5, 3),
    nodesBC[0]: (1, 3),
    nodesBC[1]: (1.5, 3),
}

# Draw the graph
plt.figure(figsize=(12, 8))

# Draw nodes
nx.draw_networkx_nodes(G, pos, node_color='skyblue', node_size=3000, alpha=0.9)

# Draw edges
nx.draw_networkx_edges(G, pos, edge_color='black', width=2, arrows=True, arrowstyle='-|>', arrowsize=20)

# Draw labels
nx.draw_networkx_labels(G, pos, font_size=10, font_weight='bold')

# Draw edge labels
edge_labels = {(u, v): f"{d['bandwidth']}, {d['delay']}" for u, v, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=8)

plt.title("Topologie Réseau avec 5 nœuds")
plt.axis('off')
plt.show()

