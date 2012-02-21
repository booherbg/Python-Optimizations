def fib(int n):
    """Calculate Fib lots of times up to N"""
    cdef int k
    cdef int a
    cdef int b
    cdef int t
    k = 0
    #while k < 1000000:
    a = 0
    b = 1
    while b < n:
        t = b
        b = a + b
        a = t
    k = k+1
    return b
    
#if __name__ == '__main__':
#    print fib(1234567890)
