def CountingSort(A, counter):
    # initialize F with 0s
    F = []
    for i in range(len(A)):
        F.append(0)

    # loop through values of A, updating F
    for i in range(len(A)):
        current_val = A[i]
        F[current_val] += 1

    # loop through indices of F, Overwrite A
    k = 0
    for i in range(len(F)):
        while F[i] > 0:
            A[k] = i
            k += 1
            F[i] -= 1