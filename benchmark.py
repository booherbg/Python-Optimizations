# quick benchmark
import os
import time
from numpy import mean

plotting = True
	
path_to_unladen_swallow = 'unladen_swallow'

tests = [('Pure C', './fib_c'),
		 ('Pure C -O3', './fib_O3c'),
		 ('Py (cpython)', 'python fib_purepython.py'),
		 ('Py (pypy)', 'pypy fib_purepython.py'),
		 ('Py (swallow)', '%s fib_purepython.py' % path_to_unladen_swallow),
		 ('Cython (def)', 'python cython_test.py'),
		 ('Cython (opt)', 'python cython_test_O3.py'),
		 ('ctypes (C)', 'python fib_ctypes.py'),
		 ('ctypes (C -O3)', 'python fib_ctypes_O3.py'),
		 ('jython (-jar)', './fib_jython.sh'),
		 ]
		

data = [] 
for label, cmd in tests:
	ret = []
	print "%s..." % label
	for i in range(3):
		t1 = time.time()
		result = os.popen(cmd).read()
		taken = time.time() - t1
		ret.append(taken)
	taken = mean(taken)
	data.append((taken, label))
	
data.sort()
data.reverse()
for d,l in data:
	print l.ljust(30), ("%.3f" % d).ljust(10), 'sec'
	
if plotting:
	data, labels = zip(*data)
	from pylab import array, bar, yticks, xticks, show, grid, arange, xlabel, ylabel, title
	xlocations = array(range(len(data)))+0.5
	width = 0.5
	bar(xlocations, data, width=width)
	yticks(arange(0, max(data)+1, .5))
	grid()
	xticks(xlocations+ width/2.0, labels)
	xlabel("Python Interpeter / Platform")
	ylabel("Time (sec)")
	title("Fib(1234567890) one million times")
	show()
