from hashlib import new


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

def sort(myList):
    sorted_list = []
    while len(myList) > 0:
        min_value = myList[0]
        c = 0
        index = 0
        for x in myList:
            if x < min_value:
                min_value = x
                index = c
            c = c + 1
        sorted_item = myList.pop(index)
        sorted_list.append(sorted_item)
    return sorted_list

def main():
    text = 'this is a test to see wether this function works out or not'
    list1 = text.split()
    list2 = [4,5,6,8,4,2,1,5,45,21,12,23,0,5,1,3,9,7,13,40]
    print(list1)
    print(list2)
    print("Counting 'this':", count(list1, 'this'))
    print("Counting 5:", count(list2, 5))
    print("is 'or' in list:", isin(list1, 'or'))
    print("is 32 in the list:", isin(list2, 32))
    print("index for 'or':", index(list1, 'or'))
    print("index for 1:", index(list2, 1))
    print('Testing reverse():')
    print(reverse(list1))
    print(reverse(list2))
    print('Testing sort():')
    print(sort(list1))
    print(sort(list2))

main()