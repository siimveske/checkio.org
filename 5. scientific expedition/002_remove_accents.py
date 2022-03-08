import unicodedata


def checkio(in_string: str):
    result = []
    for c in unicodedata.normalize('NFD', in_string):
        if unicodedata.category(c) != 'Mn':
            result.append(c)
    return ''.join(result)


if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
