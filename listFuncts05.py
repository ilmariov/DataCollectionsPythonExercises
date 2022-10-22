def count(myList, x):
    c = 0
    for i in myList:
        if i == x:
            c = c + 1
    return c

def isin(myList, x):
    for i in myList:
        if i == x:
            return True
    return False

def index(myList, x):
    c = 0
    for i in myList:
        if i == x:
            return c
        c = c + 1

def reverse(myList):
    l = len(myList)
    new_list = [0] * l
    index = l-1
    for x in myList:
        new_list[index] = x
        index = index - 1
    return new_list