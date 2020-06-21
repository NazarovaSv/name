with open('lich2.txt', 'r+', encoding ='utf-8') as d:
    l = d.readlines()
    k = 0
    h = ' '
    for i in l:
        k+=1
        print()
        print(k,i,'\n''Количество символов, включая невидеммые: ' + str(len(i)))
        if h in i:
            print('Количество слов: '+ str(len(h)+1))
        else:
            print('Количество слов: 1')
