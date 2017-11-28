#              0
#         1          2
#     3     4     5     6
#    7 8   9 10 11 12 13 14
#  15 ...                 30
# 31 ...                   62

class Heap():
    def __init__(self, input = []):
        assert type(input) == list
        self.list_form = input
        print('hey')
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

h = Heap()
print(h.list_form)

for m in range(7):
    print(h.row_limits(m))
print()

for k in [10, 20, 70, 700, 7, 8, 9, 11, 12, 13, 14]:
    print(k)
    print(h.what_coords(k))
    print(h.parent(k))
    print(h.what_coords(h.parent(k)))
    print()
print('done')
