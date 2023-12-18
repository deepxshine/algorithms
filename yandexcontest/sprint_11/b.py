def combinations(numbers):
    n = []
    answer =''
    _keys = {
        '2': ['a', 'b', 'c'],
        '3': ['d', 'e', 'f'],
        '4': ['g', 'h', 'f'],
        '5': ['j', 'k', 'l'],
        '6': ['m', 'n', 'o'],
        '7': ['p', 'q', 'r', 's'],
        '8': ['t', 'u', 'v'],
        '9': ['w','x', 'y', 'z'],
    }
    for number in numbers:
        if number in _keys.keys():
            n.append(_keys[number])

    for i in range(len(n[0])):
        f = n[0][i]
        for j in n[i]:
            answer=answer+f+j+ ' '

def read_input(string):
    return [i for i in string]


if __name__ == '__main__':
    print(combinations(read_input(input())))
