login = input()
if login[:2] =='io' and login[2:].isdigit() and len(login)<=10:
    print('Correct')
else:
    print("Incorrect")
