def ShakerSort(l, counter):
    switched = True

    while switched:
        switched = False

        # loop through left to right
        for i in range(len(l) - 1): 
            counter.add_compare()

            if l[i] > l[i + 1]: 
                counter.add_swap()

                tmp = l[i + 1]
                l[i + 1] = l[i]
                l[i] = tmp

                switched = True

        # loop through backwards
        for i in range(len(l) - 1, 0, -1): 
            counter.add_compare()

            if l[i] < l[i - 1]:
                counter.add_swap()

                tmp = l[i]
                l[i] = l[i - 1]
                l[i - 1] = tmp

                switched = True

    return l