import time
from functools import wraps


def profiling_decorator_with_unit(unit):
    def profiling_decorator(f):
        @wraps(f)
        def wrap_f(n):
            start_time = time.time()
            result = f(n)
            end_time = time.time()
            if unit == "seconds":
                elpased_time = (end_time - start_time) / 1000
            else:
                elpased_time = end_time - start_time
            print("[Time elpased for n = {}] {}".format(n, elpased_time))
            return result
        return wrap_f
    return profiling_decorator


@profiling_decorator_with_unit("seconds")
def fib(n):
    print("Inside fib")
    if n < 2:
        return
    fibPrev, fib = 1, 1
    for _ in range(2, n):
        fibPrev, fib = fib, fib + fibPrev
    return fib


if __name__ == "__main__":
    n = 77 
    print("Fibonacci number for n = {}: {}".format(n, fib(n)))