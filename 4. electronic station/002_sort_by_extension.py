'''
Sort list by the file extension. The files with the same extension should be sorted by name
    - Filename cannot be an empty string;
    - Files without the extension should go before the files with one;
    - Filename ".config" has an empty extension and a name ".config";
    - Filename "config." has an empty extension and a name "config.";
    - Filename "table.imp.xls" has an extension "xls" and a name "table.imp";
    - Filename ".imp.xls" has an extension "xls" and a name ".imp".
'''


from typing import List


def sort_by_ext(files: List[str]) -> List[str]:
    return sorted(files, key=_parse)


def _parse(item: str):
    if item.count('.') == 1:
        if item.startswith('.') or item.endswith('.'):
            return (0, item, '')
    extension = item.split('.')[-1]
    return (1, extension, item)


if __name__ == '__main__':
    assert sort_by_ext(['1.cad', '1.bat', '1.aa']) == ['1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '2.bat']) == ['1.aa', '1.bat', '2.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.bat']) == ['.bat', '1.aa', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '.aa', '.bat']) == ['.aa', '.bat', '1.bat', '1.cad']
    assert sort_by_ext(['1.cad', '1.', '1.aa']) == ['1.', '1.aa', '1.cad']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '1.aa.doc']) == ['1.aa', '1.bat', '1.cad', '1.aa.doc']
    assert sort_by_ext(['1.cad', '1.bat', '1.aa', '.aa.doc']) == ['1.aa', '1.bat', '1.cad', '.aa.doc']

    print("OK")
