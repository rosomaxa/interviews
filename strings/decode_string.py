"""Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the
square brackets is being repeated exactly k times.
Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces,
square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k.
For example, there won't be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".
"""


class Solution(object):
    def decodeString(self, s):
        stack = []
        current_num = 0
        current_str = ''
        for ch in s:
            if ch == '[':
                stack.append(current_str)
                stack.append(current_num)
                current_str = ''
                current_num = 0
            elif ch == ']':
                prev_num = stack.pop()
                prev_str = stack.pop()
                current_str = prev_str + prev_num * current_str
            elif ch.isdigit():
                current_num += current_num * 10 + int(ch)
            else:
                current_str += ch
        return current_str

    def decodeString1(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = [[1, '']]
        start = 0
        while start < len(s):
            this_char = s[start]
            if '0' <= this_char <= '9':
                digit_end = start
                while '0' <= s[digit_end] <= '9':
                    digit_end += 1
                stack += [[int(s[start:digit_end]), '']]
                start = digit_end

            elif this_char == ']':
                digit, str_ = stack.pop()
                stack[-1][1] += str_ * digit
            else:sentence-screen-fitting
                stack[-1][1] += this_char
            start += 1

        return stack[-1][1]


if __name__ == '__main__':
    assert Solution().decodeString('3[a]2[bc]') == 'aaabcbc'
    assert Solution().decodeString('3[a2[c]]') == 'accaccacc'
    assert Solution().decodeString('2[abc]3[cd]ef') == 'abcabccdcdcdef'

