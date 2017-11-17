"""Given a pattern and a string str, find if str follows the same pattern.

Here follow means a full match, such that there is a bijection between a letter
in pattern and a non-empty word in str.

Examples:
pattern = "abba", str = "dog cat cat dog" should return true.
pattern = "abba", str = "dog cat cat fish" should return false.
pattern = "aaaa", str = "dog cat cat dog" should return false.
pattern = "abba", str = "dog dog dog dog" should return false.
Notes:
You may assume pattern contains only lowercase letters,
and str contains lowercase letters separated by a single space.
"""
import unittest


class WordPatternTest(unittest.TestCase):
    def setUp(self):
        self.s = Solution()
        self.pattern = 'abba'

    def test_return_false_for_empty_str(self):
        self.assertFalse(self.s.wordPattern(self.pattern, ''))

    def test_return_false_for_empth_pattern(self):
        self.assertFalse(self.s.wordPattern('', 'foo'))

    def test_return_true_for_single_word_given_single_char_pattern(self):
        self.assertTrue(self.s.wordPattern('a', 'foo'))

    def test_return_false_for_two_words_given_single_char_pattern(self):
        self.assertFalse(self.s.wordPattern('a', 'foo bar'))

    def test_return_true_for_valid(self):
        self.assertTrue(self.s.wordPattern(self.pattern, 'dog cat cat dog'))
        self.assertTrue(self.s.wordPattern('abc', 'b c a'))

    def test_return_false_for_invalid(self):
        self.assertFalse(self.s.wordPattern(self.pattern, 'dog cat cat fish'))
        self.assertFalse(self.s.wordPattern('aaaa', 'dog cat cat dog'))
        self.assertFalse(self.s.wordPattern(self.pattern, 'dog dog dog dog'))


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not (str and pattern):
            return False

        words = str.split()
        if len(pattern) != len(words):
            return False

        pattern_to_word = {}
        word_to_pattern = {}
        for i, this_word in enumerate(words):
            this_pattern = pattern[i]
            existing_word_ind = pattern_to_word.get(this_pattern)
            existing_pattern_ind = word_to_pattern.get(this_word)
            if existing_pattern_ind != existing_word_ind:
                return False

            pattern_to_word[this_pattern] = i
            word_to_pattern[this_word] = i

        return True


if __name__ == '__main__':
    unittest.main()
