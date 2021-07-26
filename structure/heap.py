class MinHeap:
    def __init__(self):
        self.heap = []

    def __str__(self):
        return '-'.join([str(i) for i in self.heap])

    def min(self):
        return self.heap[0]

    def insert(self, value):
        self.heap.append(value)
        self.__floatUp(len(self.heap))

    def remove_min(self):
        self.__swap(0, -1)
        self.heap.pop()
        self.__drop(0)

    def __floatUp(self, index):
        while index // 2 > 0:
            if self.heap[index-1] < self.heap[index // 2-1]:
                self.__swap(index-1, index // 2-1)
            index = index // 2

    def __drop(self, index):
        while index * 2 < len(self.heap):
            smaller = self.__smaller(index)
            self.__swap(index, smaller)
            index = smaller

    def __smaller(self, index):
        if index * 2 + 1 > len(self.heap):
            return index * 2
        else:
            if self.heap[index*2+1] < self.heap[index*2]:
                return index * 2 + 1
            else:
                return index * 2

    def __swap(self, a, b):
        self.heap[a], self.heap[b] = self.heap[b], self.heap[a]

    def is_valid(self):
        n = len(self.heap)
        for i in range(2, n):
            if self.heap[i // 2] > self.heap[i]:
                return False
        return True
