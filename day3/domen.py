e = 'ga6]3-57.oi@-gmail.by.com'
email = e.split('@')
email1 = email[0]
email2 = email[1]
# e3 = email2.split('.')
# d = e.find('@')
# if int(d)>1:
#     print('incorrect')
# elif e.isdigit() or e.isalnum() or s in e and email1[-1].isalnum() or email1[-1].isdigit() and email1[0].isalnum() or email1[0].isdigit():
#      if e3[-1].isalnum() and email2[0].isalnum() or email2[0].isdigit():
#         print('correct')
# else:
#     print('incorrect')
s = ['.','_','-']
# for i in email1[0]:
#    if i in s:
#         print('not')
# for i in email1[-1]:
#    if i in s:
#         print('not')
# for i in email2[0]:
#    if i in s:
#         print('not')
# for i in email2[-1]:
#    if i in s:
#         print('not')
for i in email1:
    for j in i:
        if j in s:
            if email1[0]==j or email1[-1]==j:
                print('incorrect')
                break
        elif j.isalnum() or j in s:  # почему не исключает остальные сиволы?
            print('correct')
# for i in email2:
#     for j in i:
#         if j in s:
#             if email2[0]==j or email2[-1]==j:
#                 print('incorrect')
#                 break
#         if j.isalnum() or j in s:  # почему не исключает остальные сиволы?
#             print('correct')
