"""
Given an integer x, return true if x is a
palindrome
, and false otherwise.
"""


class Solution:
    def check_border(self, x: str):
        if x[0] != x[-1]:
            return False
        elif len(x) <= 1:
            return True
        elif len(x) == 2:
            return x[0] == x[1]

        else:
            return self.check_border(x[1:-1])

    def isPalindrome(self, x: int) -> bool:
        num_string = str(x)
        return self.check_border(num_string)


a = Solution()
print(a.isPalindrome(145))

