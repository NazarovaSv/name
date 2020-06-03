e = 'garag.uy@gmailcom.by'
email = e.split('@')
email1 = email[0]
email2 = email[1]
e3 = email2.split('.')
d = e.find('@')
s = '.-_'.split()
if int(d)>1:
    print('incorrect')
elif e.isdigit() or e.isalnum() or s in e and email1[-1].isalnum() or email1[-1].isdigit() and email1[0].isalnum() or email1[0].isdigit():
     if e3[-1].isalnum() and email2[0].isalnum() or email2[0].isdigit():
        print('correct')
else:
    print('incorrect')
