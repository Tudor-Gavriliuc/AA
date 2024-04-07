import time

import matplotlib.pyplot as plt
import pandas as pd
from networkx.generators.random_graphs import erdos_renyi_graph

from dfs_bfs import GraphDFS, GraphBFS

values=[ 4, 8, 16, 32, 64, 128, 256, 512]
timeDFS = []
timeBFS = []
for i in values:
    g = erdos_renyi_graph(i, 0.5)
    graph = GraphDFS()
    for a in g.edges:
        n,e = a
        graph.addEdge(n,e)
    start = time.perf_counter()
    graph.DFS(0)
    end = time.perf_counter()
    timeDFS.append(end - start)

plt.plot(values, timeDFS ,label="Deapth First Search")
plt.xlabel('Nr of nodes')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()

for i in values:
    g = erdos_renyi_graph(i, 0.5)
    graph = GraphBFS()
    for a in g.edges:
        n,e = a
        graph.addEdge(n,e)
    start = time.perf_counter()
    graph.bfs(0)
    end = time.perf_counter()
    timeBFS.append(end - start)

plt.plot(values, timeBFS ,label="Breadth First Search")
plt.xlabel('Nr of nodes')
plt.ylabel('Time')
plt.title('Execution Time')
plt.legend()
plt.show()

plt.plot(values, timeDFS ,label="Deapth First Search")
plt.plot(values, timeBFS ,label="Breadth First Search")
plt.xlabel('Nr of nodes')
plt.ylabel('Time (seconds)')
plt.title('Graph Traversal Algorithms')
plt.legend()
plt.show()

data = []
for i in range(len(values)):
    n = values[i]
    data.append([n, timeDFS[i], timeBFS[i]])

# Display results in a tables
headers = ["Nr of vertices", 'DFS', 'BFS']
df = pd.DataFrame(data, columns=headers)
print(df)