word = str(raw_input())
numVowel = 0
for vowel in word:
    if vowel == "a" or vowel == "e" or vowel == "i" or vowel == "o" or vowel == "u":
        numVowel += 1
print("Number of vowels: " + str(numVowel))
