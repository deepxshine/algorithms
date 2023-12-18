def step_4():
    i = 0
    while True:
        yield 4 ** i
        i += 1


def is_power_of_four(number: int) -> bool:
    for i in step_4():
        if i == number:
            return True
        elif i > number:
            return False


print(is_power_of_four(int(input())))
