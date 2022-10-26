from random import randint

def shuffle(myList):
    init_len = len(myList)
    new_list = []
    while (len(new_list) < init_len):
        index = randint(0, len(myList)-1)
        new_element = myList.pop(index)
        new_list.append(new_element)
    return new_list

def main():
    aList = ['queso', 2, 'suero', 'yuca', 56.2, 'NonSense', 'Mondongo', 8456, 'Album']
    print(aList)
    print(shuffle(aList))

main()