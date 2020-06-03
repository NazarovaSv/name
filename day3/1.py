a = '15 3'
n = '10 5'
al = a.split()
nl = n.split()
az0 = int(al[0])
az1 = int(al[1])
nz0 = int (nl[0])
nz1 = int (nl[1])
if az0/az1 > nz0/nz1:
    print(1)
elif az0/az1 == nz0/nz1:
    print(0)
else:
    print(-1)
