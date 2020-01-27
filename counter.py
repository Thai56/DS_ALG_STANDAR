class Counter:
    def __init__(self):
        self.Compares = 0
        self.Swaps = 0
    
    def add_compare(self):
        self.Compares+=1

    def add_swap(self):
        self.Swaps+=1