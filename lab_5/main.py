import time
import matplotlib.pyplot as plt
import main_algorithms as Algorithms
import pandas as pd

# Define a list of node counts to evaluate algorithms
values = [4, 8, 16, 32, 64, 128, 256, 512]
# Initialize lists to store computation times for each algorithm and graph type
timePrimSparse = []
timePrimDense = []
timeKruskalSparse = []
timeKruskalDense = []

# Create an instance of the Algorithms class
Algorithms = Algorithms.Algorithms()

# Iterate over each node count to evaluate Prim's and Kruskal's algorithms
for i in values:
    # Generate a sparse graph and measure the time it takes to run Prim's algorithm
    graph = Algorithms.generate_sparse_graph(i, i * 2)
    start = time.perf_counter()
    Algorithms.prim(graph)
    end = time.perf_counter()
    timePrimSparse.append(end - start)

    # Measure the time it takes to run Kruskal's algorithm on the same sparse graph
    start = time.perf_counter()
    Algorithms.kruskal(graph)
    end = time.perf_counter()
    timeKruskalSparse.append(end - start)

    # Generate a dense graph and measure the time for Prim's algorithm
    graph = Algorithms.generate_dense_graph(i)
    start = time.perf_counter()
    Algorithms.prim(graph)
    end = time.perf_counter()
    timePrimDense.append(end - start)

    # Measure the time for Kruskal's algorithm on the dense graph
    start = time.perf_counter()
    Algorithms.kruskal(graph)
    end = time.perf_counter()
    timeKruskalDense.append(end - start)

# Plotting the results for Prim's algorithm on sparse and dense graphs
plt.plot(values, timePrimSparse, label="Prim Sparse")
plt.plot(values, timePrimDense, label="Prim Dense")
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.title('Prim Algorithm')
plt.legend()  # Adding legend to the plot
plt.show()

# Plotting the results for Kruskal's algorithm on sparse and dense graphs
plt.plot(values, timeKruskalSparse, label="Kruskal Sparse")
plt.plot(values, timeKruskalDense, label="Kruskal Dense")
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.title('Kruskal Algorithm')
plt.legend()  # Adding legend to the plot
plt.show()

# Plotting combined results for both Prim's and Kruskal's algorithms
plt.plot(values, timePrimSparse, label="Prim Sparse")
plt.plot(values, timePrimDense, label="Prim Dense")
plt.plot(values, timeKruskalSparse, label="Kruskal Sparse")
plt.plot(values, timeKruskalDense, label="Kruskal Dense")
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.title('Minimum Spanning Tree Algorithms')
plt.legend()  # Adding legend to the plot
plt.show()

# Prepare and display a DataFrame summarizing the benchmarking results
data = []
for i in range(len(values)):
    n = values[i]
    data.append([n, timePrimSparse[i], timePrimDense[i], timeKruskalSparse[i], timeKruskalDense[i]])

df = pd.DataFrame(data, columns=["Nodes", "Prim Sparse", "Prim Dense", "Kruskal Sparse", "Kruskal Dense"])
print(df)  # Display the DataFrame
