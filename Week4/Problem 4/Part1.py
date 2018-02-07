def getWordScore(word,n):
    score = 0
    for i in word:
        score += SCRABBLE_LETTER_VALUES[i]
    if len(word) == n:
        return (score * len(word)) + 50
    else:
        return score * len(word)
