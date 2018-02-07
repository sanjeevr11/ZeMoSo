def updateHand(hand, word):
    lis = hand.copy()
    for i in word :
        if i in lis.keys():
            lis[i] -= 1
    return lis
