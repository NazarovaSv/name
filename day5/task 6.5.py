
d = 'ruN IrOn Euro SANdAy WeeK meN PaST BooK EvEryDaY'.split()
ho = {}
def f(x):
    for i in d:
        for j in i:
            if j.islower():
                if i in ho:
                    ho[i] += 1
                else:
                    ho[i] = 1

print(f(d), ho)
a = ho.values()
b = ho.keys()
for i in a:
  for o in b:
    for j in range(len(d)):
      if o == str(d[j]):
        l = d[j]
        if i> (len(l)-i):
           print(l.lower())
           break
        if i< (len(l)-i):
            print(l.upper())
            break
        else:
            print(l.title())
            break
