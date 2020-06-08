e = '.ga6]3-57.oi@-gmail.by.com'
email = e.split('@')
email1 = email[0]
email2 = email[1]

s = ['.','_','-']
for i in email1:
    for j in i:
        if j.isalnum() or j in s:
            print("correct")
        if j in s and (j == email1[0] or j == email1[-1]):
            print("Error")
            quit()
        # if (j in s and j in email1[0]) or (j in s and j in email1[-1]):
        #         print('incorrect', i)
        #         quit()
        # elif j.isalnum() or j in s:  # почему не исключает остальные сиволы?
        #     print('correct')
