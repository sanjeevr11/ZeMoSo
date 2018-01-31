def biggest(animals):
    temp = 0
    largest = None
    for i in animals.keys():
        if temp <= len(animals[i]):
            temp  = len(animals[i])
            largest = i
            
    return largest
