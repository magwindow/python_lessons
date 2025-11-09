import cython

cpdef int fib(int x):
    cdef int y = 0
    cdef int i
    for i in range(x+1):
        y += i
    return y