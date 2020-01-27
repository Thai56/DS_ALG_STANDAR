# Select the value that is smallest between within index and the end 
def SelectionSort(A, counter): 
    for i in range(len(A)):
        smallestIndex = i

        # j loops from i through end
        for j in range(i + 1, len(A)):  # mark the smallest index
            counter.add_compare() 

            if A[j] < A[smallestIndex]:
                smallestIndex = j

        counter.add_swap()

        # put next smaller index in variable smallestIndex.A[i],
        A[i], A[smallestIndex] = A[smallestIndex], A[i]

    return A
