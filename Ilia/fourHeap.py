import copy

INF = 10**14


class fourHeap(object):
    def __init__(self, heap):
        self.heap = copy.deepcopy(heap)
        if self.heap:
            self.heapify(0)

    def length(self):
        return len(self.heap)

    @staticmethod
    def get_parent_index(child_index):
        return (child_index - 1) // 4

    def heapify(self, index):
        children = self.get_children(index)
        if not children:
            return
        min_child_index = children.index(min(children))
        min_child_index = (4 * index) + (min_child_index + 1)
        if self.heap[min_child_index] < self.heap[index]:
            self.swap(index, min_child_index)
            if min_child_index <= self.length() // 4:
                self.heapify(min_child_index)

    def get_children(self, parent_index):
        children = []
        size = self.length()
        for i in range(4):
            child_index = (parent_index * 4) + (i + 1)
            if child_index < size:
                children.append(self.heap[child_index])
            else:
                break
        return children

    def sift_up(self, index):
        if index == 0:
            return
        parent = (index - 1) // 4
        if self.heap[parent] < self.heap[index]:
            return
        self.swap(parent, index)
        self.sift_up(parent)

    def get_root_value(self):
        return self.heap[0]

    def add_element(self, element):
        if isinstance(element, list):
            for _element in element:
                self.heap.append(_element)
                self.sift_up(self.length() - 1)
        else:
            self.heap.append(element)
            self.sift_up(self.length() - 1)

    def extract_root(self):
        self.swap(0, self.length() - 1)
        result = self.heap.pop()
        self.heapify(0)
        return result

    def search_by_value(self, value):
        length = self.length()
        for index in range(length):
            if self.heap[index] == value:
                return index
        return -1

    def swap(self, index1, index2):
        temp = self.heap[index1]
        self.heap[index1] = self.heap[index2]
        self.heap[index2] = temp
        
    def delete_element_by_index(self, index):
        if index >= self.length():
            return
        self.heap[index] = INF
        self.sift_up(index)
        self.extract_root()