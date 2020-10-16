def question_29(n):
    if n == 0:
        return 1
    else:
        return n * question_29(n-1)
