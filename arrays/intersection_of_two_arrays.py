"""Given two arrays, write a function to compute their intersection.

Example:
Given nums1 = [1, 2, 2, 1], nums2 = [2, 2], return [2].

Note:
Each element in the result must be unique.
The result can be in any order.
"""


def binary_search(nums, elem, start, end):
    if start > end:
        return

    mid = start + (end - start) // 2
    if nums[mid] == elem:
        return mid
    elif nums[mid] < elem:
        return binary_search(nums, elem, mid + 1, end)
    else:
        return binary_search(nums, elem, start, mid - 1)


def merge_sort(S):
    def merge(S, S1, S2):
        i = 0
        j = 0
        while (i + j) < len(S):
            if (j == len(S2)) or (i < len(S1) and S1[i] < S2[j]):
                S[i + j] = S1[i]
                i += 1
            else:
                S[i + j] = S2[j]
                j += 1

    n = len(S)
    if n < 2:
        return

    S1 = S[:n // 2]
    S2 = S[n // 2:]
    merge_sort(S1)
    merge_sort(S2)
    merge(S, S1, S2)


class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        intersection = set()
        if len(nums1) < len(nums2):
            bigger = nums2
            smaller = nums1
        else:
            bigger = nums1
            smaller = nums2

        merge_sort(smaller)
        for num in bigger:
            ind = binary_search(smaller, num, 0, len(smaller) - 1)
            if ind is not None:
                intersection.add(smaller[ind])
        return list(intersection)


if __name__ == "__main__":
    arr1 = [6, 4, 9, 0, 12, 4]
    arr2 = [0, 7, 4, 11, 6, 0]

    assert sorted(Solution().intersection(arr1, arr2)) == [0, 4, 6]
