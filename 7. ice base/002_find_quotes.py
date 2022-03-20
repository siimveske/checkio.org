'''https://py.checkio.org/en/mission/find-quotes/'''


def find_quotes(s: str) -> list:
    quotes = []
    str_length = len(s)
    start = 0
    end = 1

    while start < str_length:
        if s[start] == '"':
            while s[end] != '"':
                end += 1
            quote = s[start + 1:end]
            quotes.append(quote)
            start = end + 1
            end = start + 1
        else:
            start += 1
            end += 1

    return quotes


if __name__ == '__main__':
    assert find_quotes('"Greetings"') == ['Greetings']
    assert find_quotes('Hi') == []
    assert find_quotes('good morning mister "superman"') == ['superman']
    assert find_quotes('"this" doesn\'t make any "sense"') == ['this', 'sense']
    assert find_quotes('"Lorem Ipsum" is simply dummy text '
                       'of the printing and typesetting '
                       'industry. Lorem Ipsum has been the '
                       '"industry\'s standard dummy text '
                       'ever since the 1500s", when an '
                       'unknown printer took a galley of '
                       'type and scrambled it to make a type '
                       'specimen book. It has survived not '
                       'only five centuries, but also the '
                       'leap into electronic typesetting, '
                       'remaining essentially unchanged. "It '
                       'was popularised in the 1960s" with '
                       'the release of Letraset sheets '
                       'containing Lorem Ipsum passages, and '
                       'more recently with desktop '
                       'publishing software like Aldus '
                       'PageMaker including versions of '
                       'Lorem Ipsum.') == ['Lorem Ipsum',
                                           "industry's standard dummy text ever "
                                           'since the 1500s',
                                           'It was popularised in the 1960s']
    assert find_quotes('count empty quotes ""') == ['']
    print("OK")
