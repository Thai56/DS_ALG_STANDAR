def BubbleSort(r, counter):
    switched = True 

    while switched:
        switched = False

        for i in range(len(r) - 1):

            counter.add_compare()
            if r[i] > r[i + 1]:
                counter.add_swap()
                tmp = r[i + 1] 
                r[i + 1] = r[i]
                r[i] = tmp

                switched = True

    return r

