##cache = {0:0, 1:1}
##def fibonacci(n):
##    if n in cache:
##        return cache[n]
##    else:
##        cache[n] =  fibonacci(n - 1) + fibonacci(n - 2)
##        return cache[n]
##    
##
##print(fibonacci(50))


def memoized(f):
    cache = {}
    def wrapped(k):
        v = cache.get(k)
        if v is None:
            v = cache[k] = f(k)
        return v
    return wrapped

@memoized
def fibonacci(n):
    if n in [0, 1]:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(3))
