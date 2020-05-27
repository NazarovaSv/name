c = [7, 8, 9, 5, 4, 0]
for i in range(len(c) - 1):
    for j in range(len(c) - i - 1):
        if c[j] > c[j + 1]:
            c[j], c[j + 1] = c[j + 1], c[j]
print(c)
