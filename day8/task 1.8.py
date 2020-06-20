f = open('lich.txt',  encoding ='utf-8') # перевод в другую кадировку
# text = f.read(1) # прочесть один символ
# text2 = f.read(2) # прочесть два символа продолжит сч момента остановки на text
# text3 = f.read() # прочитает весь текст
# print(f.encoding) # проверить в какой кодировке читает винда
text = f.readlines()
print(text[0]) #выводит первую строку
print(text[5])
print(text[:5])
s1 = int(input('Начальная строка'))
s2 = int(input("Последняя строка"))
print(text[s1:s2+1])
print(text)
f.close()
