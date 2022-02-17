"""
You are given a string and two markers (the initial and final). You have to find a substring enclosed between these two markers. But there are a few important conditions:
    - The initial and final markers are always different.
    - If there is no initial marker, then the first character should be considered the beginning of a string.
    - If there is no final marker, then the last character should be considered the ending of a string.
    - If the initial and final markers are missing then simply return the whole string.
    - If the final marker comes before the initial marker, then return an empty string.
"""


def between_markers(text: str, begin: str, end: str) -> str:
    """
        returns substring between two given markers
    """
    idx_begin = text.find(begin)
    if idx_begin >= 0:
        idx_begin += len(begin)
    idx_end = text.find(end)

    result = ''
    if idx_begin >= 0 and idx_end >= 0:
        result = text[idx_begin:idx_end]
    elif idx_begin >= 0:
        result = text[idx_begin:]
    elif idx_end >= 0:
        result = text[:idx_end]
    else:
        result = text

    return result


if __name__ == '__main__':

    assert between_markers('What is >apple<', '>', '<') == "apple"
    assert between_markers("<head><title>My new site</title></head>", "<title>", "</title>") == "My new site"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi'
    assert between_markers('No <hi>', '>', '<') == ''

    print("OK")
