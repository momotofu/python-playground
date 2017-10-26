mytuple = (("a", "b", "c"), ("e", "f", "g"), ("h", "i", "j"))

def dict_from_tuple(a_tuple):
    newDict = {}
    print ("a_tuple to enumerate: ", dir(enumerate(a_tuple)))
    print(enumerate(a_tuple).next())
    for i, v in enumerate(mytuple):
        newDict[bin(i)] = v
    return newDict

print(dict_from_tuple(mytuple))
