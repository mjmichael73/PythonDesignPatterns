import time

class ProfilingDecorator(object):

    def __init__(self, f):
        self.f = f
    
    def __call__(self, *args):
        start_time = time.time() 
        result = self.f(*args)
        end_time = time.time()
        print("[Time elapsed for n = {}] {}".format(*args, end_time -start_time))
        return result

@ProfilingDecorator
def fib(n):
    if n < 2:
        return
    fibPrev, fib = 1, 1
    for _ in range(2, n):
        fibPrev, fib = fib, fib + fibPrev
    return fib

if __name__ == "__main__":
    n = 77
    print("Fibonacci number for n = {}: {}".format(n, fib(n)))