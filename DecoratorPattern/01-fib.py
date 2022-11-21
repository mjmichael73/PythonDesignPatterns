import time

n = 77
start_time = time.time()
fibPrev = 1
fib = 1

for num in range(2, n):
    fibPrev, fib = fib, fib + fibPrev

end_time = time.time()

print("[Time elpased for n = {}] {}".format(n, end_time - start_time))
print("Fibonacci number for n = {}: {}".format(n, fib))
