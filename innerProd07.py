def innerProd(x,y):
    try:
        prod_list = []
        for i in range(len(x)):
            prod = x[i] * y[i]
            prod_list.append(prod)
        return prod_list

    except:
        print('Be aware to enter two (same length) lists')

