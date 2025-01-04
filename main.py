import random
import sys
import time

sys.setrecursionlimit(20000)

case = None
version = None

def selectCase():
    global case
    print()
    print("Please select the case you want to run.")
    print("1. Average Case")
    print("2. Worst Case")
    while True:
        temp = input()
        if temp == "1":
            case = 1
            break
        elif temp == "2":
            case = 2
            break
        elif temp == "exit":
            sys.exit()
        else:
            print("Invalid Input. Please enter only 1, 2 or exit.")
            continue

def runVersion(version, arr, k):
    if version == 1:
        v1.quickselect(arr, 0, len(arr) - 1, k - 1)
    elif version == 2:
        v2.quickselect(arr, 0, len(arr) - 1, k - 1)
    elif version == 3:
        v3.permuteList(arr)
        v3.quickselect(arr, 0, len(arr) - 1, k - 1)
    elif version == 4:
        x = 5
        v4.quickselect(arr, 0, len(arr) - 1, k - 1, x)

def printForN():
    print()
    print("Enter a number to select the value of n.")
    print("1. n = 100")
    print("2. n = 1000")
    print("3. n = 10000")
    print("4. Change Case")
    
def writeToFile(arr, file):
    for j in range(len(arr)):
        if j != len(arr) - 1:
            file.write(f"{arr[j]}-")
        else:
            file.write(f"{arr[j]}\n")
    file.write("\n")

print("Please select the version of QuickSelect you want to run. Enter exit to exit the program.")
print("1. Version 1")
print("2. Version 2")
print("3. Version 3")
print("4. Version 4")

while True:
    temp = input()
    if temp == "1":
        import v1
        version = 1
        break
    elif temp == "2":
        import v2
        version = 2
        break
    elif temp == "3":
        import v3
        version = 3
        break
    elif temp == "4":
        import v4
        version = 4
        break
    elif temp == "exit":
        sys.exit()
    else:
        print("Invalid Input. Please enter only 1, 2, 3, 4 or exit.")
        continue

selectCase()
print()

while True:
    N = None
    k = None
    arr = []
    print("Current Version: Version " + str(version))
    if case == 1:
        print("Current Case: Average ")
    else:
        print("Current Case: Worst ")

    printForN()
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
        elif temp == "4":
            selectCase()
            print()
            print("Current Version: Version " + str(version))
            if case == 1:
                print("Current Case: Average ")
            else:
                print("Current Case: Worst ")
            printForN()
            continue
        elif temp == "exit":
            sys.exit()
        else:
            print("Invalid Input. Please enter only 1, 2, 3, 4 or exit.")
            continue
    
    print()
    if case == 1:
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
    else:
        k = 1

    print("Please select the type of input.")
    print("1. Type 1")
    print("2. Type 2")
    print("3. Type 3")    

    inputType = None
    numRange = None
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
    
    file = open(f"output-v{version}-{case}-{N}-{k}-{inputType}.txt", "w")
    
    if case == 1:
        totalTime = 0
        for i in range(5):
            arr = [random.randint(1, numRange) for i in range(N)]
            
            file.write(f"case: average, n: {N}, k: {k}, input type: {inputType}, input: {i + 1}\n")
            writeToFile(arr, file)
            
            startTime = time.perf_counter()
            runVersion(version, arr, k)
            totalTime += time.perf_counter() - startTime
            
        file.write(f"average time: {((totalTime / 5) * 1000):.6f}\n")
        print(f"case: average, n: {N}, k: {k}, input type: {inputType}, average time: {((totalTime / 5) * 1000):.6f}\n")

    else:
        arr = [random.randint(1, numRange) for i in range(N)]
        arr.sort()
        
        file.write(f"case: worst, n: {N}, k: {k}, input type: {inputType}\n")
        writeToFile(arr, file)
                
        startTime = time.perf_counter()
        runVersion(version, arr, k)
        endTime = time.perf_counter()
        
        file.write(f"time: {((endTime - startTime) * 1000):.6f}")
        print(f"case: worst, n: {N}, k: {k}, input type: {inputType}, time: {((endTime - startTime) * 1000):.6f}\n")
        
    file.close()