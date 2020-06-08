x = int(input())
def f(x, n):
    i = 1
    x1 = x
    while i < n:
        x = x * x1
        i += 1
    return x
print( f(x, 6) * f(x - 5, 3) / f(2 * x + 1, 5))

