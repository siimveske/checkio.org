'''
https://py.checkio.org/en/mission/verify-anagrams/
'''
from collections import defaultdict


def verify_anagrams(a: str, b: str) -> bool:
    s1 = a.replace(' ', '').lower()
    s2 = b.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    s1_letter_count = defaultdict(int)
    s2_letter_count = defaultdict(int)

    for idx in range(len(s1)):
        s1_letter_count[s1[idx]] += 1
        s2_letter_count[s2[idx]] += 1

    return s1_letter_count == s2_letter_count


if __name__ == '__main__':
    assert verify_anagrams('Programming', 'Gram Ring Mop') == True
    assert verify_anagrams('Hello', 'Ole Oh') == False
    assert verify_anagrams('Kyoto', 'Tokyo') == True

    print("OK")
