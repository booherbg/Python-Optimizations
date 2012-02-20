# quick benchmark
import os
import time
from numpy import mean

path_to_unladen_swallow = 'unladen_swallow'

tests = [('Pure C', './fib_c'),
		 ('Pure C -O3', './fib_O3c'),
		 ('Pure Python (cpython)', 'python fib_purepython.py'),
		 ('Pure Python (pypy)', 'pypy fib_purepython.py'),
		 ('Pure Python (swallow)', '%s fib_purepython.py' % path_to_unladen_swallow),
		 ('Cython (default)', 'python cython_test.py'),
		 ('Cython (optimized)', 'python cython_test_O3.py'),
		 ('ctypes (pure C)', 'python fib_ctypes.py'),
		 ('ctypes (pure C -O3)', 'python fib_ctypes_O3.py'),
		 ('jython (-jar file)', './fib_jython.sh'),
		 ]
		 
for label, cmd in tests:
	ret = []
	for i in range(10):
		t1 = time.time()
		result = os.popen(cmd).read()
		taken = time.time() - t1
		ret.append(taken)
	taken = mean(taken)
	print label.ljust(30), ("%.3f" % taken).ljust(10), 'sec'
