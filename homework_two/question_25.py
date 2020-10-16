def smallest_prime_factor(n):
    if n == 0 or n == 1:
        return None
    if (n % 2 == 0):
        return 2
    i = 3
    while i * i <= n:
        if n %i == 0:
            return i
        i += 2
    return n

dicter = {}
for value in range(0,101):
    dicter[value] = smallest_prime_factor(value)
    
