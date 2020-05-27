login = input()
h = len(login)
g = login[:2]
p = login[2:]
if g =='io' and p.isdigit() and h<=10:
    print('Correct')
else:
    print('Incorrect')
