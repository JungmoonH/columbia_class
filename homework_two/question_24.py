def largest_prime_factor(n):
    if n == 0 or n == 1:
        return None
    
    prime_factor = 1
    i = 2
    while i <= n/i:
        if n %i == 0:
            prime_factor = i
            n /= i
        else:
            i += 1
    if prime_factor < n:
        prime_factor = int(n)
    return prime_factor

dicter = {}
for value in range(0,101):
    dicter[value] = largest_prime_factor(value)
    
