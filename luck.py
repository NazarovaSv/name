
i=0
while True:

    if i>1000:
        break
    print(i)
    i+=100


n = int(input())

factorial = 1
while n > 1:
    factorial *= n
    n -= 1

    print(factorial)