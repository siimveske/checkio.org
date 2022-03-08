import unicodedata


def checkio(in_string: str):
    '''
        normalize splits accented letters in two: letter + accent
        category(c) 'Mn' contains every accent
        http://www.fileformat.info/info/unicode/category/Mn/list.htm
    '''

    result = []
    for c in unicodedata.normalize('NFD', in_string):
        if unicodedata.category(c) != 'Mn':  # a nonspacing combining mark
            result.append(c)
    return ''.join(result)


if __name__ == '__main__':
    assert checkio(u"préfèrent") == u"preferent"
    assert checkio(u"loài trăn lớn") == u"loai tran lon"
    print('Done')
