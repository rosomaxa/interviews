"""Algorithm Knuth-Morris-Pratt.

Finding substring in O(m + n)
"""


def prefix_table(str_):
    v = [0] * len(str_)
    for i in xrange(1, len(str_)):
        k = v[i - 1]
        while k > 0 and str_[i] != str_[k]:
            k = v[k - 1]

        if str_[i] == str_[k]:
            k += 1
        v[i] = k

    return v


def kmp(str_, substr):
    v = prefix_table(substr)
    k = 0
    for i in xrange(len(str_)):
        while k > 0 and str_[i] != substr[k]:
            k = v[k - 1]
        if str_[i] == substr[k]:
            k += 1
        if k == len(substr):
            return i - len(substr) + 1, i

    return -1, -1


if __name__ == '__main__':
    print kmp('xyaxybxyzx', 'xyz')
