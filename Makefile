all: fib_demo.jar fib_c fib_O3c fib_cython.so fib_cython_opt.so fib_c.so fib_O3c.so

fib_c:	fib.c
	gcc fib.c fib_main.c -o fib_c
	
fib_c.so:	fib.c
	gcc -shared -fPIC fib.c -o fib_c.so
    
fib_O3c:	fib.c
	gcc fib_main.c fib.c -O3 -o fib_O3c
	
fib_O3c.so:	fib.c
	gcc -shared -fPIC fib.c -O3 -o fib_O3c.so
    
fib_cython.so:	fib_cython.pyx
	cython fib_cython.pyx
	gcc -shared -fpic -I/usr/include/python2.6 fib_cython.c -o fib_cython.so
    
fib_cython_opt.so:	fib_cython_opt.pyx
	cython fib_cython_opt.pyx
	gcc -shared -fpic -I/usr/include/python2.6  fib_cython_opt.c -o fib_cython_opt.so
    
fib_demo.jar:	fib_purepython.py
	jythonc --core --deep --jar fib_demo.jar fib_purepython.py
	
clean:
	rm fib_c fib_O3c fib_demo.jar fib_cython.c fib_cython_opt.c *.so
	rm -rf jpywork/
	rm -rf *.pyc
