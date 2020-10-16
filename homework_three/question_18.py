def question_18(*strings):
    listing = sorted([len(string) for string in strings])
    if len(listing) %2 == 0:
        m1 = listing[len(listing)//2]
        m2 = listing[len(listing)//2 - 1]
        median = (m1 + m2)/2
    else:
        median = listing[len(listing)//2]
    return median
