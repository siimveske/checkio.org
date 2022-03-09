'''
https://py.checkio.org/en/mission/verify-anagrams/
'''


def verify_anagrams(a: str, b: str) -> bool:
    s1 = sorted(a.replace(' ', '').lower())
    s2 = sorted(b.replace(' ', '').lower())

    return s1 == s2


if __name__ == '__main__':
    assert verify_anagrams('Programming', 'Gram Ring Mop') == True
    assert verify_anagrams('Hello', 'Ole Oh') == False
    assert verify_anagrams('Kyoto', 'Tokyo') == True

    print("OK")
