'''
https://py.checkio.org/en/mission/verify-anagrams/
'''


def verify_anagrams(a, b):
    return None


if __name__ == '__main__':
    assert verify_anagrams('Programming', 'Gram Ring Mop') == True
    assert verify_anagrams('Hello', 'Ole Oh') == False
    assert verify_anagrams('Kyoto', 'Tokyo') == True

    print("OK")
