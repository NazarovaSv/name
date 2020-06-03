money = input() # int(input())
money1 = money.split(',')
m1, m2 = money1[0], money1[1]
n1,n2,n3,n4,n5,n6 = "рубль", "рубля","рублей","копейка","копейки","копеек"
if int(m1[-1]) == 1 and int(m1) != 11:
    if int(m2[-1])==1:
     print(f'{m1} {n1} {m2} {n4}')
    if 2<int(m2[-1])<5:
     print(f'{m1} {n1} {m2} {n5}')
    if int(m2[-1])>=5:
     print(f'{m1} {n1} {m2} {n6}')
elif int(m1[-1]) == 2 or int(m1[-1]) == 3 or int(m1[-1])==4:
    if int(m2[-1])==1:
     print(f'{m1} {n2} {m2} {n4}')
    if 2<int(m2[-1])<5:
     print(f'{m1} {n2} {m2} {n5}')
    if int(m2[-1])>=5:
     print(f'{m1} {n2} {m2} {n6}')
elif int(m1[-1])>=5 or int(m1) == 11:
    if int(m2[-1])==1:
     print(f'{m1} {n3} {m2} {n4}')
    if 2<int(m2[-1])<5:
     print(f'{m1} {n3} {m2} {n5}')
    if int(m2[-1])>=5:
     print(f'{m1} {n3} {m2} {n6}')
