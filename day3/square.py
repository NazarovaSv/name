a,b,c = 10, 13, 20 #int(input()),int(input()),int(input())
if a > 0 and b > 0 and c > 0 and a < 1000 and 1000 > b and c < 1000:
       # 2*z +2*x = a - где x,z стороны прямоугольника 1
       # 2*x +2*p = b - где x,р стороны прямоугольника 2
        # 2*y +2*z = c - где у,z стороны прямоугольника 3
        print(c - a + b)
