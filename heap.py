#              0
#         1          2
#     3     4     5     6
#    7 8   9 10 11 12 13 14
#  15 ...                 30
# 31 ...                   62

from random import randint

class Heap():
    def __init__(self, input = []):
        assert type(input) == list
        self.list_form = input
    def row_limits(self, m):
        return [2 ** m - 1, 2 ** (m+1) - 2]
    def what_row(self, i):
        assert i >= 0
        m_test = 0
        while(True):
            [i_low, i_high] = self.row_limits(m_test)
            if i_low <= i <= i_high:
                return m_test
            m_test += 1
    def what_col(self, i):
        m = self.what_row(i)
        [low, high] = self.row_limits(m)
        return i - low
    def what_coords(self, i):
        return [self.what_row(i), self.what_col(i)]
    def parent(self, i):
        return int((i - 1) / 2)
    def add(self, k):
        i = len(self.list_form)
        i_parent = self.parent(i)
        if len(self.list_form) > 0:
            k_parent = self.list_form[i_parent]
        self.list_form += [k]
        if len(self.list_form) > 1:
            while k > k_parent:
                self.swap(i, i_parent)
                i = i_parent
                i_parent = self.parent(i)
                k = self.list_form[i]
                k_parent = self.list_form[i_parent]
    def swap(self, i, j):
        ki = self.list_form[i]
        kj = self.list_form[j]
        self.list_form[i] = kj
        self.list_form[j] = ki

h = Heap()
for x in range(15):
    v = randint(0,100)
    h.add(v)
    print(h.list_form)
