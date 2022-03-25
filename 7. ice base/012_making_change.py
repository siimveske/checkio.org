'''https://py.checkio.org/en/mission/making-change/'''


def checkio(amount: int, coins: list[int]) -> int:
    """
        return the minimum number of coins that add up to the price
    """

    res = calculate(amount, coins, {})
    if res == float("inf"):
        return None
    else:
        return res


def calculate(amount: int, coins: list[int], memo: dict[int, int]) -> int:
    if amount in memo:
        return memo[amount]

    if amount == 0:
        return 0
    if amount < 0:
        return float("inf")

    min_cost = float("inf")
    for coin in coins:
        cost = 1 + calculate(amount - coin, coins, memo)
        if cost < min_cost:
            min_cost = cost

    memo[amount] = min_cost
    return min_cost


if __name__ == '__main__':
    assert checkio(8, [1, 3, 5]) == 2
    assert checkio(12, [1, 4, 5]) == 3
    print('OK')
