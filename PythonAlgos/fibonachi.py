def fib_bad(n):
    if n <= 2:
        f = 1
    else:
        f = fib(n-1) + fib(n-2)
    return f

def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        f = 1
    else:
        f = fib(n-1, memo) + fib(n-2, memo)
        memo[n] = f
    return f


def fib_bu(n):
    result = {}
    for i in range(1,n+1):
        if i <= 2:
            result[i] = 1
        else:
            f = result[i-1] + result[i-2]
            result[i] = f
    return result[n]

print(fib_bu(7))
