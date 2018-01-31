def oddTuples(tuples):
    t =()
    length = len(tuples)
    for i in range(0,length):
        if i%2 == 0 :
            t = t + (tuples[i],)
    return t
