import random_data
import math

class Test:
    def __init__(self, name, method, size = 10):
        self.name = name
        self.method = method
        self.size = size

    def run(self, c): 
        n = self.name
        r = random_data.CreateRandomData(self.size)
        print("// ------------------ %s - Start ------------------ \n " % (n))
        print("random_list = %s \n" % (r))
        s = sorted(r[:])
        self.method(r, c)
        print("matched = %r \n python_sorted = %s \n method_sorted = %s \n" % (r == s, r, s))
        print("// ------------------ %s - End ------------------ \n " % (n))
