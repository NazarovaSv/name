with open('lich1.txt', 'r+', encoding ='utf-8') as d, open('lich2.txt', "w+", encoding ='utf-8') as f:
    t = d.read()
    for line in t:
            if line == '0':
                f.write('1')
            elif line =='1':
                f.write('0')
            else:
                f.write(line)
