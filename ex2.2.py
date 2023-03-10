import sys
import json
import timeit
import matplotlib.pyplot as plt

sys.setrecursionlimit(20000)

def func1(arr, low, high):
    if low < high:
        pi = func2(arr, low, high)
        func1(arr, low, pi - 1)
        func1(arr, pi + 1, high)

def func2(array, start, end):
    p = array[start]
    low  = start + 1
    high = end
    while True:
        while low <= high and array[high] >= p:
            high = high - 1
        while low <= high and array[low] <= p:
            low = low + 1
        if low <= high:
            array[low], array[high] = array[high], array[low]
        else:
            break
    array[start], array[high] = array[high], array[start]
    return high


def main():

    with open("ex2.json", "r") as inF:
        content = json.load(inF)

    numb_index = count(content)#ex: [56, 84, 445]



    time_container = []
    numb_container = []
    for i, container in enumerate(content):

        time_con = timeit.timeit(lambda:  func1(container, 0, numb_index[i] - 1), number = 1)
        time_container.append(time_con)
        numb_container.append(len(container))
    
    plt.plot(numb_container, time_container, color="blue")
    plt.title("List Length of Each List in the ex2.json as a Function of Time Taken to Sort it for the Algorithm Given")
    plt.xlabel("List Length (n)")
    plt.ylabel("Time (s)")
    plt.show()


    array_ex = [43, 3432,11, 3, 545984, 32]


    func1(array_ex, 0, 2)
    print(array_ex)
    
def count(con):
    
    
    return_arr = []
    for arr in con:
        i = 0
        for x in arr:
            i += 1
        return_arr.append(i)

    
    return return_arr

if __name__ == "__main__":
    main()

    
