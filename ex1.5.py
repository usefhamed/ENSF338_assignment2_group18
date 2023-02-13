import matplotlib.pyplot as plt
import timeit
#finishing comment for commit
def fib_ori(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_ori(n - 1) + fib_ori(n - 2)

def fib(n, cache):
    if n == 0 or n == 1:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            calculate = fib(n - 1, cache) + fib(n - 2, cache)
            cache[n] = calculate
            return calculate

def fib_chat(n, cache={0: 0, 1: 1}):
    if n not in cache:
        cache[n] = fib_chat(n-1, cache) + fib_chat(n-2, cache)
    return cache[n]


def timeit_fib_ori(n):
    time = timeit.timeit(lambda: fib_ori(n), number = 25)
    return time

def timeit_fib(n, dict):
    time = timeit.timeit(lambda: fib(n, dict), number = 25)
    return time

def main():
    result_dict = {}
    
    time_fib_ori = [timeit_fib_ori(n) for n in range(36)]
    time_fib = [timeit_fib(n, result_dict) for n in range(36)]

    index = [n for n in range (36)]

    plt.plot(index, time_fib_ori, color = "red", label="Original Fibonacci Function")
    plt.plot(index, time_fib, color = "blue", label="Optimized Fibonacci Function")
    plt.title("25 Executions of Different Indexes as a Function of Time for Two Different Recursive Fibonacci Functions")
    plt.xlabel("Index (n)")
    plt.ylabel("Time (s)")
    plt.legend()
    plt.show()





if __name__ == "__main__":
    main()

