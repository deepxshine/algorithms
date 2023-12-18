from typing import List, Tuple


# 84509740
def near_zero(houses: List[int], n: int) :
    distance = [n] * n
    zero = [i for i in range(n) if houses[i] == 0]
    first = zero[0]
    last = zero[-1]

    for i in range(first, n):
        if houses[i] != 0:
            distance[i] = distance[i - 1] + 1
        else:
            distance[i] = 0
    for i in range(last, first, -1):
        if houses[i] != 0:
            distance[i] = min(distance[i], distance[i + 1] + 1)
        else:
            distance[i] = 0
    for i in range(first - 1, -1, -1):
        distance[i] = distance[i + 1] + 1
    return distance


def read_input() -> Tuple[List[int], int]:
    n = int(input())
    houses = [int(i) for i in input().split()]
    return houses, n


def main():
    houses, n = read_input()
    print(*near_zero(houses, n), sep=' ')


if __name__ == '__main__':
    main()
