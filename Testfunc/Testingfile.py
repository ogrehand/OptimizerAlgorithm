import math 

def bealefunc(n):
    # beale function
    # -4.5 <= x,y <= 4.5
    # min at 3,0.5 =>0
    x = n[0]
    y = n[1]
    return (1.5-x+(x*y))**2+(2.25-x+(x*y**2))**2+(2.625-x+(x*y**3))**2




def rastriginfunc(n):
    # rastrigin function
    # [-5.12,5.12]
    # max at 0,0 =>0
    x = n[0]
    y = n[1]
    A = 10
    return A*2 + (x**2-A*math.cos(2*math.pi*x))+(y**2-A*math.cos(2*math.pi*y))


def himmelblaufunc(n):
    # -5 <= x,y <= 5
    # min at 3.0        2.0
    # min at -2.805118  3.131312
    # min at -3.779310  -3.283186
    # min at 3.584428   -1.848126
    x = n[0]
    y = n[1]
    return (x**2+y-11)**2 + (x+y**2-7)**2
