import random_data

import bubble_sort
import shaker_sort
import selection_sort 

import quick_sort as qs
import modified_quick_sort as mqs
import counting_sort

import counter
import test 
import math

class Sort_Interface: 
    def __init__(self, name, method):
        self.name = name
        self.method = method

def main(): 
    sorts = [
        Sort_Interface("Bubble Sort", bubble_sort.BubbleSort),
        Sort_Interface("Shaker Sort", shaker_sort.ShakerSort),
        Sort_Interface("Selection Sort", selection_sort.SelectionSort),
        Sort_Interface("Quick Sort", qs.quick_sort_starter),
        Sort_Interface("Modified Quick Sort", mqs.modified_quick_sort_starter),
        Sort_Interface("Counting Sort", counting_sort.CountingSort),
    ]

    for s in range(3, 13):
        size = 2 ** s 
        print(s)

        for i in range(len(sorts)): 
            r = random_data.CreateRandomData(size)
            c = counter.Counter()
            sorts[i].method(r, c)

            compares = swaps = 0
            if c.Compares > 0:
               compares = math.log(c.Compares, 2)
            
            if c.Swaps > 0:
               swaps = math.log(c.Swaps, 2)
            print(" // ---------- %s - size = %d ---------- " % (sorts[i].name, size))
            print("compares = %d \n swaps = %d " % (compares, swaps))


if __name__ == "__main__":
    main()