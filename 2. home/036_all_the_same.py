from typing import List, Any


def all_the_same(elements: List[Any]) -> bool:

    for item in elements:
        if item != elements[0]:
            return False
    return True


def all_the_same_short(elements: List[Any]) -> bool:
    # elements = [X1,X2,X3,X4,X5]
    # elements[:-1] # [X1,X2,X3,X4]
    # elements[1:] #  [X2,X3,X4,X5]
    return elements[:-1] == elements[1:]


if __name__ == '__main__':

    assert all_the_same([1, 1, 1]) == True
    assert all_the_same([1, 2, 1]) == False
    assert all_the_same(['a', 'a', 'a']) == True
    assert all_the_same([]) == True
    assert all_the_same([1]) == True

    print("OK")
