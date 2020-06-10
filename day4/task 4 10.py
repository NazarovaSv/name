a = [4, 5, 6, 7, 8, 9, 1, 12, 3,9,7,8,15,4]
# a = input().split()
def g(x, n):
    if n < 0:
            print(a[-n:] + a[:-n])
    else:
        if n > 0:
            print(a[n:] + a[:-n-1])

print(g(a, -7), a)
