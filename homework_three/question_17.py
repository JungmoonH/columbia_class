def question_17(*strings):
    listing = [len(string) for string in strings]
    if len(listing) != 0:
        return float(sum(listing)) / len(listing)
    else:
        return None
