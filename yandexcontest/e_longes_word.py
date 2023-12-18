def get_longest_word(line: str) -> str:
    words = list(line.split())
    longest = words[0]
    for i in words:
        if len(i) > len(longest):
            longest = i
    return longest


def read_input() -> str:
    _ = input()
    line = input().strip()
    return line


def print_result(result: str) -> None:
    print(result)
    print(len(result))


print_result(get_longest_word(read_input()))
