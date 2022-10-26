from calendar import c


def removeDuplicates(aList):
    new_list = []
    for item in aList:
        if not(item in new_list):
            new_list.append(item)
    return new_list

def main():
    list = removeDuplicates([2,3,5,2,6,48,65,'as','be',59,3,5,'as',2,6,'be',7,8])
    print(list)

main()