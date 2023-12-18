# 85517886

def partition(results: list, left: int, right: int) -> int:
    pivot = results[left]
    left_border = left + 1
    right_border = right - 1
    while True:
        if left_border <= right_border and results[right_border] > pivot:
            right_border -= 1
        elif (left_border <= right_border
              and results[left_border] < pivot):
            left_border += 1
        elif (results[right_border] > pivot or
              results[left_border] < pivot):
            continue
        if left_border <= right_border:
            results[left_border], results[right_border] = results[
                right_border], results[left_border]
        else:
            results[left], results[right_border] = results[
                right_border], results[left]
            return right_border


def quick_sort(results: list, left: int, right: int):
    if (right - left) > 1:
        p = partition(results, left, right)
        quick_sort(results, left, p)
        quick_sort(results, p + 1, right)


def transformation(results: list) -> list:
    return [-int(results[1]), int(results[2]), results[0]]


if __name__ == '__main__':
    number = int(input())
    results = [transformation(input().split()) for _ in range(number)]
    left = 0
    quick_sort(results, left, len(results))
    print(*(list(zip(*results))[2]), sep="\n")
