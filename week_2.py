import random_data

# Algorithms
import quick_sort as qs
import modified_quick_sort as mqs
import counting_sort

import test
import counter 

def main():

    methods = [
        test.Test("Quick Sort", qs.quick_sort_starter),
        test.Test("Modified Quick Sort", mqs.modified_quick_sort_starter),
        test.Test("Counting Sort", counting_sort.CountingSort),
    ]

    for i in range(len(methods)):
        methods[i].run()

if __name__ == "__main__":
    main()
