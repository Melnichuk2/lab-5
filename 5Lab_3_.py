#4. Описати функцію IsPalindrome (K), що повертає True, якщо цілий параметр K (> 0) є
#паліндромом (тобто його запис читається однаково зліва направо і справа наліво), і
#False в іншому випадку. З її допомогою знайти кількість паліндромів в наборі з 10
#цілих позитивних чисел.

def Palindrom(x):
    x_str = str(x)
    revers_x_str = int(x_str[::-1])
    x_str = int(x)
    if revers_x_str == x_str:
        return True
    else:
        return False
for i in range(10):
    number = int(input("Enter numder : "))
    print(Palindrom(number))

