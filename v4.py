import random

def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

def partition(arr, left, right):
    p = arr[right]
    r = right
    l = left - 1
    while True:
        l += 1
        while arr[l] < p:
            l += 1
        r -= 1
        while arr[r] > p:
            r -= 1
        if l >= r:
            break
        else:
            swap(arr, l, r)
    swap(arr, l, right)
    pivot = l
    return pivot

def median_of_medians(arr, left, right, x):
    sublists = []
    for i in range(left, right + 1, x):
        sublists.append(arr[i:i + x])
    
    medians = []
    for sublist in sublists:
        medians.append(sorted(sublist)[len(sublist) // 2])
    
    return sorted(medians)[len(medians) // 2]

def quickselect(arr, left, right, k, x):
    if left == right:
        return arr[left]
    
    pivot_value = median_of_medians(arr, left, right, x)
    pivot_index = arr.index(pivot_value)
    swap(arr, pivot_index, right)
    pivot = partition(arr, left, right)

    if k == pivot:
        return arr[k]
    elif k < pivot:
        return quickselect(arr, left, pivot - 1, k, x)
    else:
        return quickselect(arr, pivot + 1, right, k, x)
    
