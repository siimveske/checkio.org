'''https://py.checkio.org/en/mission/feed-pigeons/'''


def checkio(food):
    minute = 0
    fed_pigeons = 0
    pigeons = 0

    while True:
        minute += 1
        old_pigeons = pigeons
        pigeons += minute

        if food < pigeons:
            remains_food = food - old_pigeons
            if remains_food > 0:
                fed_pigeons += remains_food
            break

        food -= pigeons
        fed_pigeons = pigeons

    return fed_pigeons


if __name__ == '__main__':
    assert checkio(2) == 1
    assert checkio(5) == 3
    assert checkio(10) == 6

    print('OK')
