"""

"""


class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        if digits:
            element = digits.pop()
            if element == 9:
                self.plusOne(digits)
                digits.append(0)
            else:
                digits.append(element+1)
        else:
            digits.append(1)
        return digits

digits = [9]
sol = Solution()
print(sol.plusOne(digits))