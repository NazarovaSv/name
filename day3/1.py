a, n = '10 5', '10 5'
al, nl = a.split(), n.split()
az0, az1, nz0, nz1 = int(al[0]), int(al[1]), int (nl[0]), int (nl[1])
if az0/az1 > nz0/nz1:
        print(1)
elif az0/az1 == nz0/nz1:
        print(0)
else:
        print(-1)


