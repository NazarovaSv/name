i = 0
with open('lich.txt', 'r+', encoding ='utf-8') as d:
    with open('lich2.txt', "w+", encoding ='utf-8') as f:
        with open('lich3.txt', "w+", encoding ='utf-8') as g:
            for line in d:
                i+=1
                if i%2==0:
                    f.write(line)
                else:
                    g.write(line)
                # print(i,line)
