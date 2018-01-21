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
        result = []

        def generate(s, l, r):
            if len(s) == 2 * n:
                result.append(s)
                return
            if l < n:
                generate(s + '(', l + 1, r)
            if r < l:
                generate(s + ')', l, r + 1)

        generate('', 0, 0)
        return result

    def generateParenthesis1(self, n):
        l = n
        r = n
        initial = ''
        accum = []
        self.dfs(l, r, accum, initial)
        return accum

    def dfs(self, l, r, accum, str_):
        if r < l:
            return

        if l == 0 and r == 0:
            accum.append(str_)
            return

        if l:
            self.dfs(l - 1, r, accum, str_ + '(')
        if r:
            self.dfs(l, r - 1, accum, str_ + ')')


if __name__ == '__main__':
    print Solution().generateParenthesis(3)
    print Solution().generateParenthesis1(3)
