'''
You are given a positive integer. Your function should calculate the product of the digits excluding any zeroes.

For example: The number given is 123405. The result will be 1*2*3*4*5=120
'''
import math


def checkio(number: int) -> int:
    return math.prod([int(i) for i in str(number) if int(i) > 0])


if __name__ == '__main__':
    assert checkio(123405) == 120
    assert checkio(999) == 729
    assert checkio(1000) == 1
    assert checkio(1111) == 1

    print("OK")
