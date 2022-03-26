'''https://py.checkio.org/en/mission/reverse-roman-numerals/'''


def reverse_roman(roman_string: str) -> int:
    '''Convert Roman Numerals to Decimal between 1 to 3999
    based on: https://www.geeksforgeeks.org/converting-roman-numerals-decimal-lying-1-3999/
    '''

    LOOKUP = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }

    # Initialize previous character and answer
    previous = 0
    result = 0

    # Traverse through all characters
    n = len(roman_string)
    for i in range(n - 1, -1, -1):
        letter = roman_string[i]
        current_value = LOOKUP[letter]
        # If greater than or equal to previous, add to answer
        if current_value >= previous:
            result += current_value

        # If smaller than previous, subtract from answer
        else:
            result -= current_value

        # Update previous
        previous = current_value

    return result


if __name__ == '__main__':

    assert reverse_roman('VI') == 6
    assert reverse_roman('LXXVI') == 76
    assert reverse_roman('CDXCIX') == 499
    assert reverse_roman('MMMDCCCLXXXVIII') == 3888

    print('OK')
