def question_30(n):
    if n == 0:
        return 1
    else:
        return 2**(n-1) * question_30(n-1)
