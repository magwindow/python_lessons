import work_fib
import time 

start_cy = time.time()
work_fib.fib(99999999)
end_cy = time.time()
print(f"Cython: {end_cy - start_cy}")

def fib(x):
    y = 0
    for i in range(x+1):
        y += i
    return y

start_py = time.time()
fib(99999999)
end_py = time.time()
print(f"Python: {end_py - start_py}")

print(f"Speedup: {(end_py - start_py) / (end_cy - start_cy)}")

