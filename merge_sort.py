# Given a length creates an array of integers ranging from 1 to
def MergeSort(A, counter):
    counter.add_compare()
    if len(A) == 1:
        return
    # Make a copy of left and right
    mid = len(A) // 2
    L = A[0:mid]
    R = A[mid:len(A)]

    MergeSort(L ,counter)
    MergeSort(R, counter)

    i = j = k = 0

    while i < len(L) and j < len(R):
        counter.add_compare()
        if L[i] < R[j]:
            A[k] = L[i]
            i += 1
        else:
            A[k] = R[j]
            j += 1

        k += 1

    while i < len(L):
        A[k] = L[i]
        i += 1
        k += 1

    while j < len(R):
        A[k] = R[j]
        j += 1
        k += 1