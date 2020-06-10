a = input().split(' ')#'каждый охотник желает знать, где сидит фазан'.split(' ')  #input
e = sorted(a)
l = []
print(e)
b = 'а б в г д е ё ж з и й к л м н о п р с т у ф х ц ч ш щ ъ ы ь э ю я'.split()
def f(x):
     for j in b:
       for i in a:
        if i[0] == j:
            l.append(i)
print(f(a),l) # почему выводит None?

