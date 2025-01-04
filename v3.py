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
        while r >= left and arr[r] > p:
            r -= 1
        if l >= r:
            break
        else:
            swap(arr, l, r)
            
    swap(arr, l, right)
    pivot = l
    return pivot


def quickselect(arr, left, right, k):
    if right - left <= 0:
        return arr[left]
    
    pivot = partition(arr, left, right)
    if k < pivot:
        return quickselect(arr, left, pivot - 1, k)
    elif k > pivot:
        return quickselect(arr, pivot + 1, right, k)
    else:
        return arr[pivot]

def permuteList(arr):
    for i in range(len(arr)):
        j = random.randint(0, len(arr) - 1)
        swap(arr, i, j)
        
        