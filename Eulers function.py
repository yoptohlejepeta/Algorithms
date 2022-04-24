import math

def prime(number):
    for i in range(1,round(math.sqrt(number))):
        for i in range(i,round(math.sqrt(number))):
            if (number/i).is_integer() == True:
                return False
        return True

def GCD(m,n):
    a1 = m
    a2 = n
    while a2:
        a1,a2 = a2, a1%a2
    return a1

def e_f(number):  # PRO JEDNIČKU VRACÍ NULU
    value = 0
    if prime(number):
        return number - 1
    else:
        for i in range(1,number):
            if GCD(number,i) == 1:
                value += 1
        return value

print(e_f(1))