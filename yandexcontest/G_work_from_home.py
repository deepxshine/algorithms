def to_binary(number: int) -> str:
    num = ''
    if number == 0:
        return '0'
    while number >= 1:
        j = number % 2
        num = str(j) + num
        number //= 2
    return num


def read_input() -> int:
    return int(input().strip())


print(to_binary(read_input()))
