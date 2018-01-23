"""Given a string, find the length of the longest substring without
repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3.
Note that the answer must be a substring,
"pwke" is a subsequence and not a substring.
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        answer = 0
        ch_to_ind = {}
        i = 0
        for j, num in enumerate(s):
            if num in ch_to_ind:
                i = max(i, ch_to_ind[num])

            answer = max(answer, j - i + 1)
            ch_to_ind[num] = j + 1
        return answer


if __name__ == '__main__':
    print Solution().lengthOfLongestSubstring('tmmzuxt')
    print Solution().lengthOfLongestSubstring('bbbbbbb')
    print Solution().lengthOfLongestSubstring('pwwkew')
