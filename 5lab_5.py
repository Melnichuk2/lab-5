



#Описати функцію RearRange(x, y), яка перевіряє, чи можливо переставивши букви в
#слові х отримати слово y.

def RearRange(x,y):
    x = str(input(x))
    y = str(input(y))
    if x == y :
         return True
    return False
slovo1 = input("введите первое слово :")
slovo2 = input("введите второе слово :")
if RearRange(slovo1,slovo2) == True:
    print("В принипе ок")
else :
    print("Не повезло")




