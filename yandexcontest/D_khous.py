from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    chaot = 0
    for i in range(1, len(temperatures) - 1):
        if temperatures[i - 1] < temperatures[i] > temperatures[i + 1]:
            chaot += 1
    try:
        if temperatures[0] > temperatures[1]:
            chaot += 1
        if temperatures[-1] > temperatures[-2]:
            chaot += 1
    except Exception:
        chaot += 1
    return chaot


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
