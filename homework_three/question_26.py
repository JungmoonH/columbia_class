def question_26(*number):
    new_listing = []
    total = 0
    for i in range(0, len(number)):
        total += number[i]
        new_listing.append(total)
    return new_listing
