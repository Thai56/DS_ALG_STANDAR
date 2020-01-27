# Algorithms
import bubble_sort
import shaker_sort
import selection_sort 

# Test class - consists of name, test method, and run method.
import test

def main():
    methods = [
        test.Test("Bubble Sort", bubble_sort.BubbleSort), 
        test.Test("Shaker Sort", shaker_sort.ShakerSort), 
        test.Test("Selection Sort", selection_sort.SelectionSort), 
    ]

    for i in range(len(methods)):
        methods[i].run()


if __name__ == "__main__":
    main()
