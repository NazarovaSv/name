money = input().replace('.', ',')
money1 = money.split(',')
m1, m2 = money1[0], money1[1]
n1, n2, n3, n4, n5, n6 = "рубль", "рубля", "рублей", "копейка", "копейки", "копеек"
if int(m1[-1]) == 1 and int(m1) != 11:
    y = str(f'{m1} {n1}')
if int(m1[-1]) in range(2, 4):
    y = str(f'{m1} {n2}')
if int(m1[-1]) >= 5 or int(m1) == 11:
    y = str(f'{m1} {n3}')
if int(len(m2)) == 1:
    m2 = m2 + '0'
if int(m2[-1]) == 1 and int(m2) != 11:
    print(y + ' ' + f'{m2} {n4}')
if int(m2[-1]) in range(2, 4):
    print(y + ' ' + f'{m2} {n5}')
if int(m2[-1]) >= 5 or int(m2) == 11 or int(m2[-1]) == 0:
    print(y + ' '+ f'{m2} {n6}')
