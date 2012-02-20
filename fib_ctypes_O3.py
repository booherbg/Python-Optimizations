# Not all of these are used...
from ctypes import POINTER, c_double, c_int, CDLL

so = CDLL("./fib_O3c.so")
so.argtypes = (c_int,)
so.restype = c_int
def fib(n):
	return so.fib(n)
	
if __name__ == "__main__":
	print fib(1234567890)
	
