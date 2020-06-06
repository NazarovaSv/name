def f (x):
       if x < 2 and x >= -2:
          return x**2
       if x>=2:
          return x**2+4*x+5
       else:
          return 4
e=[]
i =  0
while i <5:
  x=int(input())
  f(x)
  e.append(f(x))
  i +=1
  print(e)

for i in range(len(e) - 1):
    for j in range(len(e) - i - 1):
        if e[j] > e[j + 1]:
            e[j], e[j + 1] = e[j + 1], e[j]
print(e[-1])
