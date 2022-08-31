# Networkx

# Get started
```python
import networkx as nx
nodes = ["A","B",...]
edges = [("A","B"),("...",""),("",""),("",""),("",""),("","")]
G = nx.Graph(nodes=nodes)
G.add_edges_from(edges)

# Circular drawing
nx.draw_circular(G, with_labels=True)

# "learngraph-esk" drawing
nx.draw_spring(G, with_labels=True)
```

## Removing & Degrees
```python
nodes_to_remove = [node for node,degree in dict(G.degree()).items() if degree < 2]
G.remove_nodes_from(nodes_to_remove)
```

## Different drawing modes
<details>
<summary> Drawing Modes </summary>
`draw_circular(G, keywords)` : This gives circular layout of the graph G.
`draw_planar(G, keywords)` :] This gives a planar layout of a planar networkx graph G.
`draw_random(G, keywords)` : This gives a random layout of the graph G.
`draw_spectral(G, keywords)` : This gives a spectral 2D layout of the graph G.
`draw_spring(G, keywords)` : This gives a spring layout of the graph G.
`draw_shell(G, keywords)` : This gives a shell layout of the graph G. 
</details>
