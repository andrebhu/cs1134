import ctypes  # provides low-level arrays
def make_array(n):
    return (n * ctypes.py_object)()

class ArrayList:
    def __init__(self, iterable_object=None):
        #g
        if iterable_object:
            self.data = make_array(1)
            self.capacity = 1
            self.n = 0
            for i in iterable_object:
                self.append(i)
        else:
            self.data = make_array(1)
            self.capacity = 1
            self.n = 0

    def __len__(self):
        return self.n

    def append(self, val):
        if (self.n == self.capacity):
            self.resize(2 * self.capacity)
        self.data[self.n] = val
        self.n += 1

    def resize(self, new_size):
        new_array = make_array(new_size)
        for i in range(self.n):
            new_array[i] = self.data[i]
        self.data = new_array
        self.capacity = new_size

    def extend(self, iter_collection):
        for elem in iter_collection:
            self.append(elem)


    def __getitem__(self, ind):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        return self.data[ind]

    def __setitem__(self, ind, val):
        if (not (-self.n <= ind <= self.n - 1)):
            raise IndexError('invalid index')
        if (ind < 0):
            ind = self.n + ind
        self.data[ind] = val


    def __repr__(self):
        data_as_strings = [str(self.data[i]) for i in range(self.n)]
        return '[' + ', '.join(data_as_strings) + ']'

    def __add__(self, other):
        res = ArrayList()
        res.extend(self)
        res.extend(other)
        return res

    def __iadd__(self, other):
        self.extend(other)
        return self

    def __mul__(self, times):
        res = ArrayList()
        for i in range(times):
            res.extend(self)
        return res

    def __rmul__(self, times):
        return self * times


    #h
    def remove(self, val):
        for i in range(self.n):
            if self[i] == val:
                for j in range(i + 1, self.n):
                    self[j - 1] = self[j]
                self.n -= 1
                break
        return self


    #i
    def removeAll(self, val):
        count = 0
        for i in range(self.n):
            if self[i] == val:
                self[i] = None
                count += 1

        for i in range(self.n):
            if self[i] == None:
                for j in range(i + 1, self.n):
                    self[j - 1] = self[j]
        self.n -= count
        
        return self

arr1 = ArrayList([1, 2, 3, 2, 3, 4, 2, 2])
print(arr1)
arr1.removeAll(2)
print(arr1)
