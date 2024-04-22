import time
import matplotlib.pyplot as plt
import main_algorithms
import pandas as pd

# List of node sizes to evaluate algorithms with
values = [4, 8, 16, 32, 64, 128, 256, 512]
# Initialize lists to store computation times for each algorithm and graph type
timeDijkstraSparse = []
timeDijkstraDense = []
timeFloydWarshallSparse = []
timeFloydWarshallDense = []

# Loop through each node size to perform algorithm benchmarks
for i in values:
    # Generate a sparse graph and measure the time it takes to run Dijkstra's algorithm
    graph = main_algorithms.Algorithms.generate_sparse_graph(i, i * 2)
    start = time.perf_counter()
    main_algorithms.Algorithms.dijkstra(graph, 0)
    end = time.perf_counter()
    timeDijkstraSparse.append(end - start)  # Append the time difference to the list

    # Generate a dense graph and measure the time for Dijkstra's algorithm
    graph = main_algorithms.Algorithms.generate_dense_graph(i)
    start = time.perf_counter()
    main_algorithms.Algorithms.dijkstra(graph, 0)
    end = time.perf_counter()
    timeDijkstraDense.append(end - start)

    # Generate a sparse graph and measure the time for Floyd-Warshall algorithm
    graph = main_algorithms.Algorithms.generate_sparse_graph(i, i * 2)
    start = time.perf_counter()
    main_algorithms.Algorithms.floyd_warshall(graph)
    end = time.perf_counter()
    timeFloydWarshallSparse.append(end - start)

    # Generate a dense graph and measure the time for Floyd-Warshall algorithm
    graph = main_algorithms.Algorithms.generate_dense_graph(i)
    start = time.perf_counter()
    main_algorithms.Algorithms.floyd_warshall(graph)
    end = time.perf_counter()
    timeFloydWarshallDense.append(end - start)

# Plotting the results for Dijkstra's algorithm on sparse and dense graphs
plt.plot(values, timeDijkstraSparse, label="Dijkstra Sparse")
plt.plot(values, timeDijkstraDense, label="Dijkstra Dense")
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.title('Dijkstra Algorithm')
plt.legend()  # Adding legend to the plot
plt.show()

# Plotting the results for Floyd-Warshall algorithm on sparse and dense graphs
plt.plot(values, timeFloydWarshallSparse, label="Floyd-Warshall Sparse")
plt.plot(values, timeFloydWarshallDense, label="Floyd-Warshall Dense")
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.title('Floyd-Warshall Algorithm')
plt.legend()  # Adding legend to the plot
plt.show()

# Plotting combined results for both algorithms
plt.plot(values, timeDijkstraSparse, label="Dijkstra Sparse")
plt.plot(values, timeDijkstraDense, label="Dijkstra Dense")
plt.plot(values, timeFloydWarshallSparse, label="Floyd-Warshall Sparse")
plt.plot(values, timeFloydWarshallDense, label="Floyd-Warshall Dense")
plt.xlabel('Number of nodes')
plt.ylabel('Time (seconds)')
plt.title('Shortest Path Algorithms')
plt.legend()  # Adding legend to the plot
plt.show()

# Create and display a DataFrame to summarize the benchmarking results in a table
data = []
for i in range(len(values)):
    n = values[i]
    data.append([n, timeDijkstraSparse[i], timeDijkstraDense[i], timeFloydWarshallSparse[i], timeFloydWarshallDense[i]])

headers = ["Input Size", 'Dijkstra Sparse', 'Dijkstra Dense', 'Floyd-Warshall Sparse', 'Floyd-Warshall Dense']
df = pd.DataFrame(data, columns=headers)
print(df)  # Display the DataFrame
