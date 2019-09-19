from collections import Counter

def winner(input):
    votes = Counter(input)
    dict = {}
    for values in votes.values():
        dict[values] = []