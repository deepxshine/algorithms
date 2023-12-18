class Steak:
    def __init__(self):
        self._steak = []

    def add(self, lt):
        self._steak.insert(0, lt)

    def get(self):
        _a = ''.join(self._steak)
        self._steak.clear()
        return _a
        

def reverse_words(string: str) -> str:
    sk = Steak()
    new_string = ''
    for i in string:
        if i == ' ':
            new_string += sk.get()
            new_string += ' '

        else:
            sk.add(i)
    new_string += sk.get()
    new_string += ' '

    return new_string


test_str = 'hi my name is Billy'
print(reverse_words(test_str))
