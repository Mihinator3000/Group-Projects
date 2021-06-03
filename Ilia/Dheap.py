import copy


class Dheap(object):
    def __init__(self, k, heap):
        self.heap = copy.deepcopy(heap)
        self.k = k
        if self.heap:
            self.heapify()

    def elements(self):
        return self.heap

    def length(self):
        return len(self.heap)

    def _get_parent_index(self, child_index):
        return (child_index - 1) // self.k

    def heapify(self):
        size = self.length()
        for index in reversed(range(self._get_parent_index(child_index=(size - 1)) + 1)):
            self._heapify(index=index, size=size)

    def get_children(self, parent_index):
        children = []
        size = self.length()
        for i in range(self.k):
            child_index = (parent_index * self.k) + (i + 1)
            if child_index < size:
                children.append(self.heap[child_index])
            else:
                break
        return children

    def swim_up(self, index):
        self._swim_up(index=index)

    def get_root_value(self):
        return self.heap[0]

    def add_element(self, element):
        if isinstance(element, list):
            for _element in element:
                self.heap.append(_element)
                self.swim_up(self.length() - 1)
        else:
            self.heap.append(element)
            self.swim_up(self.length() - 1)

    def extract_root(self):
        self._swap(0, self.length() - 1)
        result = self.heap.pop()
        self._heapify(index=0, size=self.length())
        return result

    def search_value(self, value):
        length = self.length()
        for index in range(length):
            if self.heap[index] == value:
                return index
        return -1

    def _swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp


class MaxHeap(Dheap):
    def __init__(self, k, heap=None):
        super(self.__class__, self).__init__(k=k, heap=heap)
        if heap is None:
            heap = []

    def _heapify(self, index, size):
        children = self.get_children(index)
        if not children:
            return
        max_child_index = children.index(max(children))
        max_child_index = (self.k * index) + (max_child_index + 1)
        if self.heap[max_child_index] > self.heap[index]:
            self._swap(index, max_child_index)
            if max_child_index <= size // self.k:
                self._heapify(max_child_index, size)

    def _swim_up(self, index):
        if index == 0:
            return
        parent = (index - 1) // self.k
        if self.heap[parent] > self.heap[index]:
            return
        self._swap(parent, index)
        self._swim_up(index=parent)

    def delete_element_at_index(self, index):
        if index >= self.length():
            return
        self.heap[index] = float("inf")
        self.swim_up(index)
        self.extract_root()