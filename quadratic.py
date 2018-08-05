a = int(input('请输入a'))
b = int(input('请输入b'))
c = int(input('请输入c'))
print ('一元二次方程为:%sx^2+ %sx+%s=0的根为:'%(a,b,c))
import math
def quadratic (a,b,c):
    if a == 0:
        if b != 0:
            return(-c/b ,无)
        elif c == 0:
            return(任何值,任何值)
        else:
            return(无,无)
    else:
        x1 = (-b + (b**2-4*a*c)**0.5)/2*a
        x2 = (-b - (b**2-4*a*c)**0.5)/2*a
        return(x1,x2)
print(quadratic(a,b,c))