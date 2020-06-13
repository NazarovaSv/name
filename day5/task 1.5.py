t = 'после ливня ты можешь увидеть радугу или увидеть солнце или шторм или еще что-нибудь'.split()
r = ''
di = {}
for i in t:
    if len(r)< len(i):
        r = i
    if i in di:
        di[i] += 1
    else:
        di[i] = 1

print(r, di)


