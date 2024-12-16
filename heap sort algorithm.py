            # heap sort
def heapify(arr, n, i):
    largest = i  # Assume the current node is the largest
    left = 2 * i + 1  # Left child index
    right = 2 * i + 2  # Right child index

    # Check if left child exists and is greater than root
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Check if right child exists and is greater than root
    if right < n and arr[right] > arr[largest]:
        largest = right

    # If the largest element is not the root
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Swap
        # Recursively heapify the affected subtree
        heapify(arr, n, largest)

# Heap Sort algorithm
def heap_sort(arr):
    n = len(arr)

     
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

     
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]   
        heapify(arr, i, 0)    

# Example usage
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    print("Array before sorting:", arr)
    heap_sort(arr)
    print("Array after sorting:", arr)
