#4. Описати функцію RingS (R1, R2) дійсного типу, яка знаходить площу кільця,
#укладеного між двома колами із загальним центром і радіусами R1 і R2 (R1 і R2 -
#дійсні, R1> R2). З її допомогою знайти площі трьох кілець, для яких дані зовнішні і
#внутрішні радіуси. Скористатися формулою площі круга радіусу R: S = π · R2


import random
import math

def RingS(R1, R2):
    return math.pi*(R1**2 - R2**2)

def CircleS(R):
    return math.pi*R**2

for i in range(0, 3):
    print(i)
    L = sorted(random.sample(range(1, 10), 2), reverse=True)
    print(L)
    print("R_1={0}:R_2={1}".format(L[0], L[1]))
    print("площадь круга1:", CircleS(L[0]))
    print("площадь круга2:", CircleS(L[1]))
    print("площадь кольца:", RingS(L[0], L[1]))


