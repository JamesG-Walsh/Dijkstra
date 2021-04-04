import math
import logging
logging.basicConfig(level=logging.DEBUG)


class Heap:
    def __init__(self, keys, n):
        self.n = n
        self.A = keys
        self.H = {}

        i = 1
        while(i <= n - 1):
            self.H[i] = None
            i += 1

        i = 1
        while (i <= n):
            self.H[i + n - 1] = i
            i += 1
        print("H: ", self.H)

        i = n - 1
        while(1 <= i):
            left = self.A[self.H[2*i]]
            right = self.A[self.H[2*i + 1]]
            print("L: ", left, "\tR: ", right)
            if(self.A[self.H[2*i]] < self.A[self.H[2*i + 1]]):
                self.H[i] = self.H[2*i]
                print("L H[", i, "]= ", self.H[i])
            else:
                self.H[i] = self.H[2*i + 1]
                print("R H[", i, "]= ", self.H[i])
            i -= 1
        print("H: ", self.H)
        print("A: ", self.A)

    def __in_heap(self, id):
        if self.H[id + self.n - 1] == 0:  # element has been extracted
            return False
        elif(id < 1 or self.n < id):  # id out of bounds
            return False
        else:
            return True

    def __min_key(self):
        return self.A[self.H[1]]

    def __min_id(self):
        return self.H[1]

    def __key(self, id):
        return self.A[id]

    def __delete_min(self):  # aka extract_min()
        self.A[0] = float('inf')
        self.H[self.H[1] + self.n - 1] = 0
        v = self.A[self.H[1]]
        i = math.floor((self.H[1] + self.n - 1) / 2)
        while(i >= 1):
            if(self.A[self.H[2*i]] <= self.A[self.H[2*i + 1]]):
                self.H[i] = self.H[2*i]
            else:
                self.H[i] = self.H[2*i + 1]
        return v

    def __decrease_key(self, id, new_key):
        if (self.A[id] <= new_key):
            return  # no update required
        self.A[id] = new_key
        i = math.floor((id + self.n - 1) / 2)
        while(i >= 1):
            if(self.A[self.H[2*i]] < self.A[self.H[2*i + 1]]):
                self.H[i] = self.H[2*i]
            else:
                self.H[i] = self.H[2*i + 1]
            i = math.floor(i / 2)
