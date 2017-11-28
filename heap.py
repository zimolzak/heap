#              0
#         1          2
#     3     4     5     6
#    7 8   9 10 11 12 13 14
#  15 ...                 30
# 31 ...                   62

from random import randint

class Heap():
    def __init__(self):
        self.list_form = []
    def _parent(self, i):
        """What list element is the parent of element i?"""
        return int((i - 1) / 2)
    def add(self, k):
        """Add an element to the heap, making sure it still satisfies the heap
        property.
        """
        i = len(self.list_form)
        i_parent = self._parent(i)
        if len(self.list_form) > 0:
            k_parent = self.list_form[i_parent]
        self.list_form += [k]
        if len(self.list_form) > 1:
            while k > k_parent:
                self._swap(i, i_parent)
                i = i_parent
                i_parent = self._parent(i)
                k = self.list_form[i]
                k_parent = self.list_form[i_parent]
    def _swap(self, i, j):
        """Swap elements i and j."""
        ki = self.list_form[i]
        kj = self.list_form[j]
        self.list_form[i] = kj
        self.list_form[j] = ki
    def pretty_str(self):
        """Return a string that emphasizes ply of the heap/tree."""
        s = ''
        for i, k in enumerate(self.list_form):
            x = 1
            while x < i:
                x *= 2
            if i + 2 == x or i == 0 or i == 2:
                s = s + str(k) + ', '
            else:
                s = s + str(k) + ' '
        return s

if __name__ == '__main__':
    h = Heap()
    for x in range(20):
        v = randint(0,100)
        h.add(v)
        print(h.pretty_str())
