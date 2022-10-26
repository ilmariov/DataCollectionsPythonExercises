def innerProd(x,y):
    try:
        prod_list = []
        for i in range(len(x)):
            prod = x[i] * y[i]
            prod_list.append(prod)
        return prod_list

    except:
        print('Be aware to enter two (same length) lists')


def main():
    list1 = [2,3,4,'fire',6,7,3,8,9]
    list2 = [1,10,11,12,13,14,'a',15,16]
    prod = innerProd(list1, list2)
    print(prod)


main()