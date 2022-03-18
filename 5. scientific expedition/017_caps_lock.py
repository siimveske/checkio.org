'''
https://py.checkio.org/en/mission/caps-lock/
'''


def caps_lock(text: str) -> str:
    caps_lock_on = False
    buffer = []
    for i in text:
        if i == 'a':
            caps_lock_on = not caps_lock_on
        elif caps_lock_on:
            buffer.append(i.upper())
        else:
            buffer.append(i)
    return ''.join(buffer)


if __name__ == "__main__":
    assert caps_lock("Why are you asking me that?") == "Why RE YOU sking me thT?"
    assert caps_lock("Always wanted to visit Zambia.") == "AlwYS Wnted to visit ZMBI."
    assert caps_lock("Aloha from Hawaii") == "Aloh FROM HwII"
    print("OK")
