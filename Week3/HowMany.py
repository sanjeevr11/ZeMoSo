def HowMany(animals):
    ans = 0
    for i in animals.values():
        ans += len(i)
    return ans
