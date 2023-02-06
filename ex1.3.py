import timeit
#finishing comment for commit
def fib2(n, cache={}):
    if n == 0 or n == 1:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            cache[n] = fib2(n-1) + fib2(n-2)
            return cache[n]

def fib_memo(n, memo={}):
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
        return memo[n]

def func(n, cache):
    if n == 0 or n == 1:
        return n
    else:
        if n in cache:
            return cache[n]
        else:
            calculate = func(n - 1, cache) + func(n - 2, cache)
            cache[n] = calculate
            return calculate

def main():
    resultm = {}
    result_func = {}
    n = 29

    fib2_time = timeit.timeit(lambda: fib2(100), number = 10)
    fibm_time = timeit.timeit(lambda: fib_memo(100, resultm), number = 10)
    func_time = timeit.timeit(lambda: func(100, result_func), number = 10)


    #func(n, result_dict)
    

    print(fib2_time)
    print(fibm_time)
    print(func_time)
   




if __name__ == "__main__":
    main()


