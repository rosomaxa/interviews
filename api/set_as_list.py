import abc
import unittest


class MySet(object):
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def is_in_set(self, x):
        pass

    @abc.abstractmethod
    def adjoin(self, x):
        pass

    @abc.abstractmethod
    def intersection(self, other):
        pass

    @abc.abstractmethod
    def union(self, other):
        pass


class SetAsUnorderedList(MySet):
    def __init__(self, *args):
        if args:
            self._my_set = list(args)
        else:
            self._my_set = []

    @property
    def my_set(self):
        return self._my_set

    def is_in_set(self, x, ind=0):
        if ind >= len(self.my_set):
            return False

        if self.my_set[ind] == x:
            return True

        return self.is_in_set(x, ind + 1)

    def adjoin(self, x):
        if not self.is_in_set(x):
            self._my_set.append(x)

        return self.my_set

    def intersection(self, other, this_set=None):
        if not other:
            return []

        if this_set is None:
            this_set = self.my_set

        if not this_set:
            return []

        if self.is_in_set(other[0]):
            return [other[0]] + self.intersection(other[1:], this_set)

        return self.intersection(other[1:], this_set)

    def union(self, other, this_set=None):
        if this_set is None:
            this_set = self.my_set

        if not this_set:
            return other or []

        if not other:
            return this_set or []

        if not self.is_in_set(other[0]):
            return [other[0]] + self.union(other[1:], this_set)

        return self.union(other[1:], this_set)


class SetAsOrderedList(SetAsUnorderedList):
    def _get_ind_to_insert(self, x, start, end):
        if self.my_set[start] >= x:
            return start
        if self.my_set[end] <= x:
            return end

        mid = start + (end - start) // 2
        if self.my_set[mid] < x:
            return self._get_ind_to_insert(x, mid + 1, end)

        return self._get_ind_to_insert(x, start, mid - 1)

    def is_in_set(self, x, ind=0):
        if not self.my_set:
            return False

        ind = self._get_ind_to_insert(x, 0, len(self.my_set) - 1)
        return self.my_set[ind] == x

    def adjoin(self, x):
        if not self.my_set:
            self.my_set.append(x)
            return self.my_set

        if not self.is_in_set(x):
            start = 0
            end = len(self.my_set) - 1
            ind = self._get_ind_to_insert(x, start, end)
            if ind == end:
                self.my_set.append(x)
            else:
                self.my_set.insert(ind, x)

        return self.my_set

    def intersection(self, other, this_set=None):
        if not other:
            return []

        if this_set is None:
            this_set = self.my_set

        if not this_set:
            return []

        x1 = other[0]
        x2 = this_set[0]
        if x1 == x2:
            return [x1] + self.intersection(other[1:], this_set[1:])

        if x1 < x2:
            return self.intersection(other[1:], this_set)

        return self.intersection(other, this_set[1:])

    def union(self, other, this_set=None):
        if this_set is None:
            this_set = self.my_set

        if not this_set:
            return other or []

        if not other:
            return this_set or []

        x1 = other[0]
        x2 = this_set[0]
        if x1 == x2:
            return [x1] + self.union(other[1:], this_set[1:])

        if x1 < x2:
            return [x1] + self.union(other[1:], this_set)

        return [x2] + self.union(other, this_set[1:])


class SetAsUnorderedListTest(unittest.TestCase):
    def setUp(self):
        self.actual_set = [4, 9, 1, 3, 7]
        self.set_ = SetAsUnorderedList(*self.actual_set)

    def test_return_true_if_element_in_set(self):
        self.assertTrue(self.set_.is_in_set(4))
        self.assertTrue(self.set_.is_in_set(7))
        self.assertTrue(self.set_.is_in_set(1))

    def test_return_false_if_element_is_missing_in_set(self):
        self.assertFalse(self.set_.is_in_set(0))
        self.assertFalse(self.set_.is_in_set(2))

    def test_adjoin_element_if_not_already_in_set(self):
        self.set_.adjoin(0)
        expected_set = self.actual_set + [0]

        self.assertEquals(self.set_.my_set, expected_set)

    def test_dont_adjoin_element_if_already_in_set(self):
        self.set_.adjoin(9)
        expected_set = self.actual_set

        self.assertEquals(self.set_.my_set, expected_set)

    def test_return_intersection_as_common_elements(self):
        other_set = [2, 4, 3, 7, 0]
        expected_set = [4, 3, 7]

        actual_set = self.set_.intersection(other_set)

        self.assertEquals(expected_set, actual_set)

    def test_empty_intersection_given_no_common_elements(self):
        other_set = [2, 0, 5]
        expected_set = []

        actual_set = self.set_.intersection(other_set)

        self.assertEquals(expected_set, actual_set)

    def test_return_non_empty_set_as_union_given_other_as_empty_set(self):
        other_set = []
        expected_union = self.actual_set

        actual_union = self.set_.union(other_set)

        self.assertEquals(expected_union, actual_union)

    def test_return_union_as_join_of_two_non_empty_sets_with_uniq_elems(self):
        other_set = [2, 0, 5]
        expected_union = other_set + self.actual_set

        actual_union = self.set_.union(other_set)

        self.assertEquals(expected_union, actual_union)

    def test_return_union_as_join_with_uniq_elems_given_non_empty_sets_with_duplicates(self):
        other_set = [4, 2, 9, 0, 5]
        expected_union = [2, 0, 5] + self.actual_set

        actual_union = self.set_.union(other_set)

        self.assertEquals(expected_union, actual_union)


class SetAsOrderedListTest(unittest.TestCase):
    def setUp(self):
        self.actual_set = [1, 3, 4, 7, 9]
        self.set_ = SetAsOrderedList(*self.actual_set)

    def test_return_true_if_element_in_set(self):
        self.assertTrue(self.set_.is_in_set(9))
        self.assertTrue(self.set_.is_in_set(7))
        self.assertTrue(self.set_.is_in_set(1))

    def test_return_false_if_element_is_missing_in_set(self):
        self.assertFalse(self.set_.is_in_set(0))
        self.assertFalse(self.set_.is_in_set(2))

    def test_adjoin_new_element_less_than_min_as_head(self):
        expected_set = [0] + self.actual_set

        self.set_.adjoin(0)

        self.assertEquals(expected_set, self.set_.my_set)

    def test_adjoin_new_element_greater_than_max_as_tail(self):
        expected_set = self.actual_set + [10]

        self.set_.adjoin(10)

        self.assertEquals(expected_set, self.set_.my_set)

    def test_insert_new_element_in_right_spot_given_no_such_elements(self):
        new_element = 5
        expected_set = [1, 3, 4, 5, 7, 9]

        self.set_.adjoin(new_element)

        self.assertEquals(expected_set, self.set_.my_set)

    def test_return_empty_intersection_given_other_as_empty(self):
        other = []
        expected_intersection = []

        actual_intersection = self.set_.intersection(other)

        self.assertEquals(expected_intersection, actual_intersection)

    def test_return_empty_intersection_given_no_common_elements(self):
        other = [2, 5, 10]
        expected_intersection = []

        actual_intersection = self.set_.intersection(other)

        self.assertEquals(expected_intersection, actual_intersection)

    def test_return_intersection_given_common_elements(self):
        other = [1, 3, 9, 11]
        expected_intersection = [1, 3, 9]

        actual_intersection = self.set_.intersection(other)

        self.assertEquals(expected_intersection, actual_intersection)

    def test_return_union_as_origin_given_empty_other(self):
        other = []
        expected_union = self.actual_set

        actual_union = self.set_.union(other)

        self.assertEquals(expected_union, actual_union)

    def test_return_union_as_join_given_no_common_elements(self):
        other = [0, 2, 8, 10]
        expected_union = [0, 1, 2, 3, 4, 7, 8, 9, 10]

        actual_union = self.set_.union(other)

        self.assertEquals(expected_union, actual_union)

    def test_return_union_as_join_of_uniq_elems_given_overlapping_elems(self):
        other = [1, 2, 5, 9, 10]
        expected_union = [1, 2, 3, 4, 5, 7, 9, 10]

        actual_union = self.set_.union(other)

        self.assertEquals(expected_union, actual_union)

if __name__ == '__main__':
    unittest.main()
