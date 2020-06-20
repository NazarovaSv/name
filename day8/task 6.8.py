with open('lich2.txt', 'r+', encoding ='utf-8') as d:
    with open('lich1.txt', "r+", encoding ='utf-8') as f:
        t = d.readlines()
        h = f.readlines()
        l = 0
        for i in t:
           l+=1
           if i in h:
                    continue
           else:
                    print(l,i)
