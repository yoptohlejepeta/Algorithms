def GCD(m,n):
    a1 = m
    a2 = n
    while a2:
        a1,a2 = a2, a1%a2
    return f'Největší společný dělitel čísel {m} a {n} je číslo {a1}. '

print(GCD(3997,2947))
# Největší společný dělitel čísel 3997 a 2947 je číslo 7.