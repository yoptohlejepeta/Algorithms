def GCD(m,n):
    a1 = m
    a2 = n
    while a2:
        a1,a2 = a2, a1%a2
    return f'Greatest common divisor of numbers {m} and {n} is {a1}. '


print(GCD(3997,2947))
# Greatest common divisor of numbers 3997 and 2947 is 7.

def GCD2(m,n):
    a = [m,n]
    b = [0,1]
    c = [1,0]
    iteration = 0
    while a[1]:
        b[0], b[1] = b[1], b[0] + b[1]*int(a[0]/a[1])
        c[0], c[1] = c[1], c[0] + c[1]*int(a[0]/a[1])
        a[0], a[1] = a[1], a[0]%a[1]
        iteration += 1
    if iteration % 2 == 0:
        return f'Greatest common divisor is {a[0]} = {(b[1] - b[0])}x{n} - {(c[1] - c[0])}x{m}'
    else:
        return f'Greatest common divisor is {a[0]} = {(c[1] - c[0])}x{m} - {(b[1] - b[0])}x{n}'

print(GCD2(3997,2947))
#Greatest common divisor is 7 = 334x3997 - 453x2947