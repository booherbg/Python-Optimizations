def fib(n):
    """Calculate Fib lots of times up to N"""
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
    
if __name__ == '__main__':
    for i in xrange(1000000):
        fib(1234567890)
