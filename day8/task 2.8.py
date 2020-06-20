with open('lich1.txt', 'w', encoding ='utf-8') as d:
    d.writelines('%s\n'%input() for i in range(6))
d.close()
