import random
import sys
import time

# swapping function
def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp

# partition function common for all versions
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

# default quickselect function for v1 and v3
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

# modified quicksleect function for v2
def quickselectV2(arr, left, right, k):
    if right - left <= 0:
        return arr[left]

    # random pivot selection
    pivot_index = random.randint(left, right)
    swap(arr, pivot_index, right)
    pivot = partition(arr, left, right)

    if k < pivot:
        return quickselectV2(arr, left, pivot - 1, k)
    elif k > pivot:
        return quickselectV2(arr, pivot + 1, right, k)
    else:
        return arr[pivot]

# modified quickselect function for v4
def quickselectV4(arr, left, right, k, x):
    if left == right:
        return arr[left]
    
    # median of medians pivot selection
    pivot_value = median_of_medians(arr, left, right, x)
    pivot_index = arr.index(pivot_value)
    swap(arr, pivot_index, right)
    pivot = partition(arr, left, right)

    if k == pivot:
        return arr[k]
    elif k < pivot:
        return quickselectV4(arr, left, pivot - 1, k, x)
    else:
        return quickselectV4(arr, pivot + 1, right, k, x)

# function to permute the list for v3
def permuteList(arr):
    for i in range(len(arr)):
        j = random.randint(0, len(arr) - 1)
        swap(arr, i, j)

# function to find the median of medians for v4
def median_of_medians(arr, left, right, x):
    sublists = []
    for i in range(left, right + 1, x):
        sublists.append(arr[i:i + x])
    
    medians = []
    for sublist in sublists:
        medians.append(sorted(sublist)[len(sublist) // 2])
    
    return sorted(medians)[len(medians) // 2]

# function to write the array to the file
def writeToFile(arr, file):
    for j in range(len(arr)):
        if j != len(arr) - 1:
            file.write(f"{arr[j]}-")
        else:
            file.write(f"{arr[j]}\n")

# function to run the versions and write the results to the file
def runVersion(file, arrays, k, versionNum):
    totalTime = 0
    # run the versions 5 times and calculate the average time
    for arr in arrays:
        if versionNum == 1:
            startTime = time.perf_counter()
            quickselect(arr, 0, len(arr) - 1, k)
            totalTime += time.perf_counter() - startTime
        if versionNum == 2:
            startTime = time.perf_counter()
            quickselectV2(arr, 0, len(arr) - 1, k)
            totalTime += time.perf_counter() - startTime
        if versionNum == 3:
            permuteList(arr)
            startTime = time.perf_counter()
            quickselect(arr, 0, len(arr) - 1, k)
            totalTime += time.perf_counter() - startTime
        if versionNum == 4:
            startTime = time.perf_counter()
            quickselectV4(arr, 0, len(arr) - 1, k, 5)
            totalTime += time.perf_counter() - startTime
    if len(arrays) == 1:
        file.write(f"Version{versionNum} Worst={(totalTime * 1000):.4f}\n")
    else:
        file.write(f"Version{versionNum} Average={(totalTime / 5 * 1000):.4f}\n")

# set the recursion limit to 20000 to avoid RecursionError
sys.setrecursionlimit(20000)

while True:
    print("Enter a number to select the value of n. Write 'exit' to exit the program.")
    print("1. n = 100")
    print("2. n = 1000")
    print("3. n = 10000")
    N = None
    k = None

    while True:
        temp = input()
        if temp == "1":
            N = 100
            break
        elif temp == "2":
            N = 1000
            break
        elif temp == "3":
            N = 10000
            break
        elif temp == "exit":
            sys.exit()
        else:
            print("Invalid Input. Please enter only 1, 2, 3 or exit.")
            continue
    
    print()
    print("Enter a number to select the value of k.")
    print("1. k = 1")
    print("2. k = n/2")
    print("3. k = n-1")
    
    while True:
        temp = input()
        if temp == "1":
            k = 1
            break
        elif temp == "2":
            k = N // 2
            break
        elif temp == "3":
            k = N - 1
            break
        elif temp == "exit":
            sys.exit()
        else:
            print("Invalid Input. Please enter only 1, 2, 3 or exit.")

    print()

    print("Please select the type of input.")
    print("1. Type 1")
    print("2. Type 2")
    print("3. Type 3")    

    inputType = None
    numRange = None
    # set the range of the random numbers based on the input type
    while True:
        temp = input()
        if temp == "1":
            inputType = 1
            numRange = 10 * N
            break
        elif temp == "2":
            inputType = 2
            numRange = 3 * N // 4
            break
        elif temp == "3":
            inputType = 3
            numRange = N // 4
            break
        elif temp == "exit":
            sys.exit()
        else:
            print("Invalid Input. Please enter only 1, 2, 3 or exit.")
            continue

    print()
    
    # open the file to write the output
    file = open(f"output-{N}-{inputType}-{k}.txt", "w")

    # generate 5 random arrays
    randomArrays = []
    for i in range(5):
        randomArrays.append([random.randint(1, numRange) for i in range(N)])
        
    file.write(f"n = {N}, Input Type{inputType}\n")
    file.write(f"k = {k}\n")
    
    # write the random arrays to the file
    for i in range(len(randomArrays)):
        file.write(f"Input{i + 1} (average) = ")
        writeToFile(randomArrays[i], file)
    
    # run all the versions
    runVersion(file, randomArrays, k, 1)
    runVersion(file, randomArrays, k, 2)
    runVersion(file, randomArrays, k, 3)
    runVersion(file, randomArrays, k, 4)
    
    # write the worst case input to the file
    file.write("\n")
    if k == 1:
        worstArr = [[random.randint(1, numRange) for i in range(N)]]
        worstArr[0].sort()
        for arr in worstArr:
            file.write(f"Input (worst) = ")
            writeToFile(arr, file)
            
        runVersion(file, worstArr, k, 1)
        runVersion(file, worstArr, k, 2)
        runVersion(file, worstArr, k, 3)
        runVersion(file, worstArr, k, 4)
        
    file.close()