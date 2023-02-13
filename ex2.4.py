import random
import json
import timeit
import matplotlib .pyplot as plt

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi - 1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    pivot = random.choice(array[start:end + 1])
    low = start
    high = end
    while low <= high:
        while array[low] < pivot:
            low += 1
        while array[high] > pivot:
            high -= 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
            low += 1
            high -= 1
    return low

def main():
    with open("ex2.json", "r") as inF:
        content = json.load(inF)

    time_complexity = []
    array_length = []

    for array in content:
        l = len(array)
        time_req = timeit.timeit(lambda: func1(array, 0, l - 1), number = 1)
        time_complexity.append(time_req)
        array_length.append(len(array))
    
    plt.plot(array_length, time_complexity, color="blue")
    plt.title("List Length of Each list in the ex2.json as a Function of Time Taken to Sort it for the Optimized Algorithm")
    plt.xlabel("List Length (n)")
    plt.ylabel("Time (s)")
    plt.show()

if __name__=="__main__":
    main()   