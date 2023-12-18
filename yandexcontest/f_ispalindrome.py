def is_palindrome(line: str) -> bool:
    sym = [i.lower() for i in line if i.isalpha()]
    return sym == list(reversed(sym))


print(is_palindrome(input().strip()))
