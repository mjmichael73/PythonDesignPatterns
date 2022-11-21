import time


def fib(n):
    if n < 2:
        return
    fibPrev, fib = 1, 1
    for num in range(2, n):
        fibPrev, fib = fib, fib + fibPrev
    return fib


def profile_me(f, n):
    start_time = time.time()
    result = f(n)
    end_time = time.time()
    print(f"[Elapsed time for n = {n} : {end_time - start_time}]")
    return result


if __name__ == "__main__":
    n = 77
    print(f"Fibonacci number for n = {n} : {profile_me(fib, n)}")
