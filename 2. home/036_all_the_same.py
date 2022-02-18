from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:

    for item in elements:
        if item != elements[0]:
            return False
    return True


if __name__ == '__main__':

    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True

    print("OK")
