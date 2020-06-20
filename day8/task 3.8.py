with open('lich1.txt', 'a', encoding ='utf-8') as d:
    d.writelines('%s\n'%input() for i in range(3))
d.close()
