"""
Given a time represented in the format "HH:MM",
form the next closest time by reusing the current digits.
There is no limit on how many times a digit can be reused.

You may assume the given input string is always valid.
For example, "01:34", "12:09" are all valid. "1:34", "12:9" are all invalid.

Example 1:

Input: "19:34"
Output: "19:39"
Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
which occurs 5 minutes later.  It is not 19:33,
because this occurs 23 hours and 59 minutes later.

Example 2:

Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since
it is smaller than the input time numerically.
"""


class Solution(object):
    def _get_next_greater_digit(self, current, upper, candidates):
        if current == upper:
            return candidates[0]

        next_ind = candidates.index(current) + 1
        if next_ind == len(candidates):
            return candidates[0]

        next_digit = candidates[next_ind]

        while (next_ind < len(candidates) and
               (next_digit > upper or next_digit == current)):
            next_ind += 1
            if next_ind == len(candidates):
                return candidates[0]

            next_digit = candidates[next_ind]

        return next_digit

    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        result = list(time)
        # Retrieve all four digits from given string and sort them in asc order
        options = sorted(filter(lambda x: x.isdigit(), time))
        position_to_upper_bound = {0: '1', 1: '9', 3: '5', 4: '9'}

        if time[0] == '2':
            position_to_upper_bound[0] = '2'
            position_to_upper_bound[1] = '3'

        for i in xrange(len(time) - 1, -1, -1):  # go from right to left
            this_upper = position_to_upper_bound.get(i)
            if this_upper is None:
                continue

            existing_digit = time[i]
            next_digit = self._get_next_greater_digit(
                existing_digit, this_upper, options)
            result[i] = next_digit

            if next_digit > existing_digit:
                break

        return ''.join(result)


if __name__ == '__main__':
    s = Solution()
    assert s.nextClosestTime("14:29") == "14:41"
    assert s.nextClosestTime("19:34") == "19:39"
    assert s.nextClosestTime("23:59") == "22:22"
    assert s.nextClosestTime("22:23") == "22:32"
    assert s.nextClosestTime("13:55") == "15:11"
