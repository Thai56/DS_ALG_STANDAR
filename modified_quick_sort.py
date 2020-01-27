# how does professor know that the params are 4 bytes each? pointer to array, and ints
def ModifiedQuickSort(A, low, high, counter):
    counter.add_compare()

    # base case
    if high - low <= 0:
        return

    counter.add_swap()

    # modified
    mid = (low + high) // 2 
    A[low], A[mid] = A[mid], A[low]

    lmb = low + 1

    # do 1 pass
    for i in range(low + 1, high + 1):
        counter.add_compare()

        if A[i] < A[low]:
            counter.add_swap()

            A[i], A[lmb] = A[lmb], A[i]
            lmb += 1

    pivot = lmb - 1

    counter.add_swap()
    A[low], A[pivot] = A[pivot], A[low]

    # recurse
    ModifiedQuickSort(A, low, pivot - 1, counter)
    ModifiedQuickSort(A, pivot + 1, high, counter)

def modified_quick_sort_starter(r, counter):
     return ModifiedQuickSort(r, 0, len(r) - 1, counter)
