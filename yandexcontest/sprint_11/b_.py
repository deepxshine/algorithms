from typing import List, Tuple


# 84598855


def get_max_points(matrix: List[str], k: int) -> int:
    points = 0
    for t in range(1, 10):
        if 0 < matrix.count(str(t)) <= k * 2:
            points += 1
    return points


def read_input() -> Tuple[List[str], int]:
    k = int(input())
    matrix = [i for i in range(4) for i in input().strip()]
    return matrix, k


def main():
    matrix, k = read_input()
    print(get_max_points(matrix, k))


if __name__ == '__main__':
    main()
