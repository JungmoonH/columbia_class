def question_11(string):
    listing = string.split()
    count = 0
    for i in listing:
        if i.isdigit():
            count += 1
    return count
