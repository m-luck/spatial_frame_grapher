import networkx as nx
G = nx.Graph()
G.add_node(2)
G.add_nodes_from([2, 3])
G.add_edge(1,2)
G.add_edge(2,1)

print(G.number_of_nodes())
print(G.number_of_edges())

print(list(G.nodes))
print(list(G.edges))
