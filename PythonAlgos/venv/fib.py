'''

def fib(n):
    if n <= 1:
        return n
    return (fib(n-1) + fib(n-2))

print fib(1)
'''



FibArray = [0, 1]

def fib(n):
    if n <= 0:
        print("Incorrect input")
    elif n <= len(FibArray):
        return FibArray[n - 1]
    else:
        temp_fib = fib(n - 1) + fib(n - 2)
        FibArray.append(temp_fib)
        return temp_fib

    # Driver Program


print(fib(10))



import timeit

class Memoclass(object):
    def __init__(self,func):
        self.f=func
        self.casche={}
    def __call__(self,*args):
        if not args in self.casche:
            self.casche[args]=self.f(*args)
        return self.casche[args]
def factor(n):
    if n==0:
        return 1
    else: return n*factor(n-1)

def fibon(n):
    if isinstance(n, int):
        if n<=0: raise ValueError("Expected number is positive integer")
        if n==1 or n==2: return 1
        else: return fibon(n-1)+fibon(n-2)
    else: raise TypeError("Incorrect type. Expected number is positive integer")

memo_fibon= Memoclass(fibon)
print memo_fibon(10)