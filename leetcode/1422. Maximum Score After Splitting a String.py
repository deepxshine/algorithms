"""Given a string s of zeros and ones, return the maximum score after splitting
 the string into two non-empty substrings (i.e. left substring and right
  substring).

The score after splitting a string is the number of zeros in the left
substring plus the number of ones in the right substring."""


class Solution:
    def maxScore(self, s: str) -> int:
        return max(
            [(s[:i].count('0') + s[i:].count('1')) for i in range(1, len(s))])
