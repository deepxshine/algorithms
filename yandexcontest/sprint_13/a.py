# 85518028

def broken_search(nums: list, target: int) -> int:
    left_border = 0
    right_border = len(nums) - 1
    while left_border <= right_border:
        middle_border = (left_border + right_border) // 2
        if target == nums[middle_border]:
            return middle_border
        if nums[middle_border] <= nums[right_border]:
            if nums[middle_border] < target <= nums[right_border]:
                left_border = middle_border + 1
            else:
                right_border = middle_border - 1
        else:
            if nums[left_border] <= target < nums[middle_border]:
                right_border = middle_border - 1
            else:
                left_border = middle_border + 1
    return -1


def test():
    arr = [19, 21, 100, 101, 1, 4, 5, 7, 12]
    assert broken_search(arr, 5) == 6


if __name__ == '__main__':
    test()
