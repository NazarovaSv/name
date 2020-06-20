import random
def mat(b,n):
    data = []
    data1 = []
    sum1 = []
    for i in range (0,b):
        strot = []
        strot1 = []
        sum2 = []
        for j in range (0,n):
             strot.append(random.randrange(0, 50))
             strot1.append(random.randrange(0, 50))
             l = int(strot[j])+int(strot1[j])
             sum2.append(l)


        sum1.append(changer)
        data.append(strot)
        data1.append(strot1)
    print(data,  data1, sum1, sep= '\n')
mat(4,4)   