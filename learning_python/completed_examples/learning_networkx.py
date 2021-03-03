# Understand the basics of the networkx software
# Started with tutorial at: https://networkx.github.io/documentation/stable/tutorial.html

import matplotlib.pyplot as plt
import networkx as nx
from random import randint

# Create graph object
G = nx.Graph()

# Create and add nodes
max_nodes = 25
node_list = [x for x in range(max_nodes)]
# print(node_list)
G.add_nodes_from(node_list)

# Create and add edges (node connections)
max_connections = 150
edge_list = [(randint(0, max_nodes-1), randint(0, max_nodes-1)) for x in range(max_connections)]
G.add_edges_from(edge_list)

# Print diagnostics
print(f"Number of nodes: {G.number_of_nodes()}")
print(f"Number of connections: {max_connections}")
print(f"Number of edges: {G.number_of_edges()}")

print(f"Edges added: {edge_list}")
print(f"Unique edges: {G.edges}")

if True:

    # Visualize various plot types
    # ptypes = [nx.draw, nx.draw_networkx, nx.draw_networkx_nodes, nx.draw_networkx_edges, nx.draw_networkx_labels, nx.draw_networkx_edge_labels, nx.draw_circular, nx.draw_kamada_kawai, nx.draw_random, nx.draw_spectral, nx.draw_spring, nx.draw_shell]
    #ptypes = [nx.draw, nx.draw_networkx, nx.draw_circular, nx.draw_kamada_kawai, nx.draw_random, nx.draw_spectral, nx.draw_spring, nx.draw_shell]
    ptypes = [nx.draw, nx.draw_networkx, nx.draw_kamada_kawai, nx.draw_spring]

    # It looks like the nx.draw_networkx, kamada_kawai look the best
    for i in ptypes:
        fig1, ax1 = plt.subplots(1)
        i(G, with_labels=True)
        ax1.set_title(i)
    plt.show()

