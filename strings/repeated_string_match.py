"""Given two strings A and B, find the minimum number of times A has to be
repeated such that B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times ("abcdabcdabcd"),
B is a substring of it; and B is not a substring of A repeated
two times ("abcdabcd").
"""
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        A_extended = A
        count = 1

        if B in A_extended:
            return count

        while True:
            A_extended += A
            count += 1
            if B in A_extended:
                return count

            if len(A_extended) > len(B):
                return -1


if __name__ == '__main__':
    print Solution().repeatedStringMatch("abcd", "cdabcdab")
