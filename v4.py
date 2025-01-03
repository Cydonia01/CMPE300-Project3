def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]


def partition(arr, left, right, pivot_index):
    pivot_value = arr[pivot_index]
    swap(arr, pivot_index, right)  # Move pivot to end
    store_index = left
    for i in range(left, right):
        if arr[i] < pivot_value:
            swap(arr, i, store_index)
            store_index += 1
    swap(arr, store_index, right)  # Move pivot to its final place
    return store_index


def median_of_medians(arr, left, right, x):
    sublists = [arr[i:i + x] for i in range(left, right + 1, x)]
    medians = [sorted(sublist)[len(sublist) // 2] for sublist in sublists]
    if len(medians) <= x:
        return sorted(medians)[len(medians) // 2]
    return median_of_medians(medians, 0, len(medians) - 1, x)


def quickselect(arr, left, right, k, x):
    if left == right:  # Only one element in the array
        return arr[left]
    
    # Find pivot using the median of medians
    pivot_value = median_of_medians(arr, left, right, x)
    pivot_index = arr.index(pivot_value)  # Get index of the pivot value

    # Partition the array around the pivot
    pivot_index = partition(arr, left, right, pivot_index)

    # Recursively search in the appropriate partition
    if k == pivot_index:
        return arr[k]
    elif k < pivot_index:
        return quickselect(arr, left, pivot_index - 1, k, x)
    else:
        return quickselect(arr, pivot_index + 1, right, k, x)


# Example usage
arr = [10, 4, 5, 8, 6, 11, 26]
k = 3  # Find the 3rd smallest element (index 2 in 0-based indexing)
x = 5  # Sublist size

result = quickselect(arr, 0, len(arr) - 1, k - 1, x)
print(f"The {k}-th smallest element is: {result}")
