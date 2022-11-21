import time

def fib(n):
    if n < 2:
        return
    fibPrev, fib = 1, 1
    for _ in range(n):
        fibPrev, fib = fib, fib + fibPrev
    return fib


def profile_me(f, n):
    start_time = time.time()
    result = f(n)
    end_time = time.time()
    print(f"[Elapsed time for n = {n}: {end_time - start_time}]")
    return result

def get_profiled_function(f):
    return lambda n: profile_me(f, n)


if __name__ == "__main__":
    n = 77
    fib_profiled = get_profiled_function(fib)
    print(f"Fibonacci number for n = {n}: {fib_profiled(n)}")