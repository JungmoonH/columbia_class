def recursive(n):
    if n == 0:
        return 1
    else:
        return 2**(n-1) * recursive(n-1)
