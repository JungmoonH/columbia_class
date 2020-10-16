def question_24(*number):
    if len(set(number)) == len(number):
        return "No mode"
    else:
        return max(set(number), key = number.count)
