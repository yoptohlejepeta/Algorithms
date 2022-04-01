def GCD(m,n):
    a1 = m
    a2 = n
    while a2:
        a1,a2 = a2, a1%a2
    return f'Greatest common divider of numbers {m} and {n} is {a1}. '


print(GCD(3997,2947))
# Greatest common divider of numbers 3997 and 2947 is 7.