def getGuessedWord(secretWord, lettersGuessed):
    letters = set(lettersGuessed)
    secret = list(secretWord)
    for i in range(0,len(secret)):
        if secret[i] not in letters :
            secret[i]='_'
    res = ''.join(secret)
    return res
