t = [1,3,5,8,9,15,4,2,3,4]
for i in range(len(t)-1):
    for j in range(i+1, len(t)):
        if t[i] == t[j]:
            print("Одно и тоже")
            quit()
print("уникум")



