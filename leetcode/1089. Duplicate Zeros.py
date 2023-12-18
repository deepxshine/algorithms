"""
Given a fixed-length integer array arr, duplicate each occurrence of zero,
 shifting the remaining elements to the right.

Note that elements beyond the length of the original array are not written.
Do the above modifications to the input array in place and do not return anything.
"""


class Solution:
    def duplicateZeros(self, arr: list[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                arr.pop()
                arr.insert(i+1, 0)
                i += 1
            i += 1
        return arr



arr = [1,0,2,3,0,4,5,0]
s = Solution()
print(s.duplicateZeros(arr))