'''
Find the TOP most expensive goods. The amount we are looking for will be given as a first argument and the whole data as the second one
'''


def bigger_price(limit: int, data: list) -> list:
    """
        TOP most expensive goods
    """
    sorted_list = sorted(data, key=lambda d: d['price'], reverse=True)
    return sorted_list[:limit]


if __name__ == '__main__':

    assert bigger_price(2, [
        {"name": "bread", "price": 100},
        {"name": "wine", "price": 138},
        {"name": "meat", "price": 15},
        {"name": "water", "price": 1}
    ]) == [
        {"name": "wine", "price": 138},
        {"name": "bread", "price": 100}
    ]  # "First"

    assert bigger_price(1, [
        {"name": "pen", "price": 5},
        {"name": "whiteboard", "price": 170}
    ]) == [{"name": "whiteboard", "price": 170}]  # "Second"

    print("OK")
