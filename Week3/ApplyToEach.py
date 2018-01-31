def applyToEach(L, f):
    for i in range(len(L)):
        if i%2 != 0 :
            L[i] = f(L[i])


def positive(x):
    return -x
    
applyToEach(testList,positive)
