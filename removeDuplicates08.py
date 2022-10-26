from calendar import c


def removeDuplicates(aList):
    new_list = []
    for item in aList:
        if not(item in new_list):
            new_list.append(item)
    return new_list
