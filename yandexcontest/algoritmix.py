# from typing import List, Tuple, Optional
#
#
# def two_sum(arr: List[int], target_sum: int) -> Optional[Tuple[int, int]]:
#     for i, j in enumerate(arr):
#         y = target_sum - j
#         if y in arr and arr.index(y) != i:
#             return (j, y)
#     return None
#
#
# def read_input() -> Tuple[List[int], int]:
#     n = int(input())
#     arr = list(map(int, input().strip().split()))
#     target_sum = int(input())
#     return arr, target_sum
#
#
# def print_result(result: Optional[Tuple[int, int]]) -> None:
#     if result is None:
#         print(None)
#     else:
#         print(" ".join(map(str, result)))
#
#
# arr, target_sum = read_input()
# print_result(two_sum(arr, target_sum))

def get_least_primes_linear(n):
    lp = [0] * (n + 1)
    primes = []
    for i in range(2, n + 1):
        if lp[i] == 0:
            lp[i] = i
            primes.append(i)
        for p in primes:
            x = p * i
            if (p > lp[i]) or (x > n):
                break
            lp[x] = p
    return primes, lp


get_least_primes_linear(8)