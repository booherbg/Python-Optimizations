int fib(int n) 
{
    //Calculate Fib lots of times up to N"""
    int k = 0;
    int a=0;
    int b=1;
    int t=0;
    while (k < 1000000)
    {
        a = 0;
        b = 1;
        while (b < n)
        {
            t = b;
            b = a + b;
            a = t;
        }
        k = k+1;
    }
    return b;
}

