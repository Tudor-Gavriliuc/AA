import time
import matplotlib.pyplot as plt
import random

class Algorithms:
    def init(self, random_list):
        self.random_list = random_list

    def bubbleSort(self):
        # Implementation of Bubble Sort algorithm
        n = len(self.random_list)
        for i in range(n):
            for j in range(0, n-i-1):
                if self.random_list[j] > self.random_list[j+1]:
                    self.random_list[j], self.random_list[j+1] = self.random_list[j+1], self.random_list[j]

    def quickSort(self):
        # Implementation of Quick Sort algorithm
        if len(self.random_list) <= 1:
            return self.random_list
        else:
            pivot = self.random_list[0]
            less = [i for i in self.random_list[1:] if i <= pivot]
            greater = [i for i in self.random_list[1:] if i > pivot]
            return Algorithms(less).quickSort() + [pivot] + Algorithms(greater).quickSort()

    def mergeSort(self):
        if len(self.random_list) <= 1:
            return self.random_list

        mid = len(self.random_list) // 2
        left_half = self.random_list[:mid]
        right_half = self.random_list[mid:]

        left_half = Algorithms(left_half).mergeSort()
        right_half = Algorithms(right_half).mergeSort()

        return self.merge(left_half, right_half)

    def merge(self, left, right):
        merged = []
        left_index = right_index = 0

        while left_index < len(left) and right_index < len(right):
            if left[left_index] < right[right_index]:
                merged.append(left[left_index])
                left_index += 1
            else:
                merged.append(right[right_index])
                right_index += 1

        merged.extend(left[left_index:])
        merged.extend(right[right_index:])

        return merged

    def heapSort(self):
        n = len(self.random_list)

        for i in range(n // 2 - 1, -1, -1):
            self.heapify(self.random_list, n, i)

        for i in range(n - 1, 0, -1):
            self.random_list[i], self.random_list[0] = self.random_list[0], self.random_list[i]
            self.heapify(self.random_list, i, 0)

        return self.random_list

    def heapify(self, arr, n, i):
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[left] > arr[largest]:
            largest = left

        if right < n and arr[right] > arr[largest]:
            largest = right

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            self.heapify(arr, n, largest)

# Define different list sizes
list_sizes = [100, 1000, 10000, 100000, 1000000]

# Initialize lists to store time taken by each algorithm for each list size
quickSort_time, mergeSort_time, heapSort_time, bubbleSort_time = [], [], [], []

# Loop through each list size
for size in list_sizes:
    # List for testing algorithms
    random_list = [random.random() for _ in range(size)]

    # Measure time taken by each sorting algorithm
    start_time = time.perf_counter()
    Algorithms(random_list).quickSort()
    end_time = time.perf_counter()
    quickSort_time.append(end_time - start_time)

    start_time = time.perf_counter()
    Algorithms(random_list).mergeSort()
    end_time = time.perf_counter()
    mergeSort_time.append(end_time - start_time)

    start_time = time.perf_counter()
    Algorithms(random_list).heapSort()
    end_time = time.perf_counter()
    heapSort_time.append(end_time - start_time)

    start_time = time.perf_counter()
    Algorithms(random_list).bubbleSort()
    end_time = time.perf_counter()
    bubbleSort_time.append(end_time - start_time)

# Plotting the results
x = list_sizes
y = [quickSort_time, mergeSort_time, heapSort_time, bubbleSort_time]
labels = ['Quick Sort', 'Merge Sort', 'Heap Sort', 'Bubble Sort']

for i in range(len(y)):
    plt.plot(x, y[i], label=labels[i])
    plt.scatter(x, y[i])
    plt.xlabel('List Size')
    plt.ylabe