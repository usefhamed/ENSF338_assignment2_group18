import random
import json
import timeit
import matplotlib .pyplot as plt

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(array, start, end):
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

def insertion_sort(array, start, end):
    for i in range(start + 1, end + 1):
        key = array[i]
        j = i - 1
        while j >= start and array[j] > key:
            array[j + 1] = array[j]
            j -= 1
        array[j + 1] = key

def sort(array):
    n = len(array)
    if n < 10:
        insertion_sort(array, 0, n - 1)
    else:
        quick_sort(array, 0, n - 1)
    return array


def main():
    with open("ex2.json", "r") as inF:
        content = json.load(inF)

    time_complexity = []
    array_length = []

    for array in content:
        time_req = timeit.timeit(lambda: sort(array), number = 1)
        time_complexity.append(time_req)
        array_length.append(len(array))
    
    plt.plot(array_length, time_complexity, color="blue")
    plt.title("Time Taken to Sort the Lists in JSON (Optimized)")
    plt.xlabel("List Length")
    plt.ylabel("Time")
    plt.show()

if __name__=="__main__":
    main()   