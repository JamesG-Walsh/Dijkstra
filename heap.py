import math
import logging
logging.basicConfig(level=logging.DEBUG)

class heap:
    def __init__(self, keys, n):
        self.nV = n
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
            L = self.A[self.H[2*i]]
            R = self.A[self.H[2*i + 1]]
            print("L: ", L, "\tR: ", R)
            if(self.A[self.H[2*i]] < self.A[self.H[2*i + 1]]):
                self.H[i] = self.H[2*i]
                print("L H[", i, "]= ", self.H[i])
            else:
                self.H[i] = self.H[2*i + 1]
                print("R H[", i, "]= ", self.H[i])
            i -= 1
        print("H: ", self.H)


    def __in_heap(self, id):
        2   # TODO search H contents?

    def __min_key(self):
        return self.A[self.H[1]]

    def __min_id(self):
        return self.H[1]

    def __key(self, id):
        return self.A[id]

    def __delete_min(self):
        6

    def __decrease_key(self, id, new_key):
        if (self.A[id] <= new_key):
            return  # no update required
        self.A[id] = new_key
        id = math.floor((id + self.nV - 1) / 2)
        while(id >= 1):
            if(self.A[self.H[2*id]] < self.A[self.H[2*id + 1]]):
                self.H[id] = self.H[2*id]
            else:
                self.H[id] = self.H[2*id + 1]
            id = math.floor(id / 2)
