def QuickSort(A, lo, hi, counter):
    counter.add_compare()

    # base case - when there is nothing left to sort.
    if hi - lo <= 0:
        return

    # lmb - left most biggest number
    lmb = lo + 1

    # Move lower numbers to the left side lmb.
    for i in range(lo + 1, hi + 1): 
        counter.add_compare()

        if A[i] < A[lo]:
            counter.add_swap()

            # A[i] is lower than our pivot swap.
            A[lmb], A[i] = A[i], A[lmb]
            lmb += 1

    # place all numbers smaller than pivot on the left side.
    pivot = lmb - 1

    counter.add_swap()
    A[lo], A[pivot] = A[pivot], A[lo]

    QuickSort(A, lo, pivot - 1, counter)
    QuickSort(A, pivot + 1, hi, counter)

def quick_sort_starter(r, counter):
     return QuickSort(r, 0, len(r) - 1, counter)
