def getAvailableLetters(lettersGuessed):
    temp = 'abcdefghijklmnopqrstuvwxyz'
    res = ''
    letters = set(lettersGuessed)
    for i in temp:
        if i not in letters:
            res = res + i
    return res
