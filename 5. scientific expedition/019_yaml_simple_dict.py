'''https://py.checkio.org/en/mission/yaml-simple-dict/'''


def yaml(a: str) -> dict:
    result = {}
    for line in a.splitlines():
        if line:
            key, value = line.split(': ')
            value = int(value) if value.isnumeric() else value
            result[key] = value
    return result


if __name__ == '__main__':
    assert yaml("""name: Alex
age: 12""") == {'age': 12, 'name': 'Alex'}
    assert yaml("""name: Alex Fox
age: 12

class: 12b""") == {'age': 12,
                   'class': '12b',
                   'name': 'Alex Fox'}
    print("OK")
