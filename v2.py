import random

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, left, right, pivot_index):
    pivot_value = arr[pivot_index]
    # Move pivot to the end
    swap(arr, pivot_index, right)
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            swap(arr, i, store_index)
            store_index += 1
    # Move pivot to its final place
    swap(arr, store_index, right)
    return store_index

def quickselect(arr, left, right, k):
    if left == right:  # If the list contains only one element
        return arr[left]

    # Choose a random pivot index
    pivot_index = random.randint(left, right)

    # Partition the array around the pivot
    pivot_index = partition(arr, left, right, pivot_index)

    # The pivot is in its final sorted position
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        # Recur on the left subarray
        return quickselect(arr, left, pivot_index - 1, k)
    else:
        # Recur on the right subarray
        return quickselect(arr, pivot_index + 1, right, k)

# Example usage
arr = [10, 4, 5, 8, 6, 11, 26]
k = 3  # Find the 3rd smallest element (0-based index, so k-1 is passed)
result = quickselect(arr, 0, len(arr) - 1, k - 1)
print(f"The {k}-th smallest element is: {result}")
