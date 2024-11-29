import time

start = time.time()

def BubbleSort(arr):
    for i in range(len(arr) - 1):  # Outer loop for passes
        for j in range(len(arr) - 1 - i):  # Inner loop for comparisons
            if arr[j] > arr[j + 1]:  # Swap if elements are in the wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr  # Return the sorted array

if __name__ == "__main__":
    arr = [4, 5, 3, 1, 2]
    print(f"Original Array: {arr}")

    output = BubbleSort(arr)
    print(f"Sorted Array: {output}")

end = time.time()


result = end - start

print(result)