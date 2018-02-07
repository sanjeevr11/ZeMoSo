def calculateHandlen(hand):
    sum = 0
    for value in hand.values():
        sum += value
    return sum
