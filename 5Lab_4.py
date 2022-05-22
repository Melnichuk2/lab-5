#Описати функцію Exp1 (x, ε) дійсного типу (параметри x, ε - дійсні, ε> 0),
#знаходить наближене значення функції exp (x):
#exp (x) = 1 + x + x2
#/ (2!) + x3
#/ (3!) + ... + xn
#/ (n!) + ...
#(N! = 1 · 2 · ... · n). В сумі враховувати всі складові, більші за ε. За допомогою Exp1
#знайти наближене значення експоненти для даного x при шести даних ε.

import random
import math
def Exp1(x,eps):
    if eps <= 0:
        print(" Epsilon should be greater than 0")
    y = x
    exp = 1.0 + x
    i = 2
    while abs(y) > eps:
        y *= x/i
        i += 1
        exp += y
    return exp

eps = 0.01
for i in range (0,6):
    x = 1
    print("eps=", eps, "; e^",x,"=",Exp1(x,eps),";",math.exp(x))
    eps /= 10