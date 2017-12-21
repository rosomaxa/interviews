"""
Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""


class Solution(object):
    def generateParenthesis(self, n):
        def generate(this_str, left, right, accum=[]):
            if left:
                generate(this_str + '(', left - 1, right)
            if right > left:
                generate(this_str + ')', left, right - 1)
            if right == 0:
                accum.append(this_str)
            return accum

        return generate('', n, n)


if __name__ == '__main__':
    print Solution().generateParenthesis(3)
