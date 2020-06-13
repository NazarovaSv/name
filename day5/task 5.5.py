n, a, b, z = 3, 2, 4, 6  # int(input()), int(input()), int(input()), int(input())
i = 0
x1 = 0
for i in range(n):
    # z, b, a=int(input()), int(input()), int(input())
    x = z ** 3 - b + a ** 2
    x1 = x1 + x
    i += 1
print(x1)
