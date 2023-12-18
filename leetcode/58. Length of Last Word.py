"""
Given a string s consisting of words and spaces, return the length of the last
word in the string.

A word is a maximal
substring
 consisting of non-space characters only.



Example 1:

Input: s = "Hello World"
Output: 5
Explanation: The last word is "World" with length 5.
"""


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        new_s = ''
        for i in (s.strip()[::-1]):
            if i == ' ' and not new_s:
                continue
            if i == ' ':
                break
            new_s += i

        return len(new_s)




sol = Solution()
l = "Hello Worldd   "
print(sol.lengthOfLastWord(l))
