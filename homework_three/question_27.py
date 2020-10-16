def question_27(*number):
    new_listing = []
    for i in range(len(number)-1):
        diff = number[i+1] - number[i]
        new_listing.append(diff)
    return new_listing
