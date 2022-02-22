'''
https://py.checkio.org/en/mission/flatten-dict/
You are given a dictionary where the keys are strings and the values are strings or dictionaries. The goal is flatten the dictionary, but save the structures in the keys. The result should be the a dictionary without the nested dictionaries. The keys should contain paths that contain the parent keys from the original dictionary. The keys in the path are separated by a "/". If a value is an empty dictionary, then it should be replaced by an empty string ("")
'''


def flatten(dictionary: dict):
    if not dict:
        return dictionary

    result = {}
    for key, value in dictionary.items():
        if type(value) is dict:
            if fdict := flatten(value):
                for key2, val2 in fdict.items():
                    new_key = f"{key}/{key2}"
                    result[new_key] = val2
            else:
                result[key] = ""
        else:
            result[key] = value

    return result


if __name__ == "__main__":
    assert flatten({"key": "value"}) == {"key": "value"}, "Simple"
    assert flatten({"key": {"deeper": {"more": {"enough": "value"}}}}) == {"key/deeper/more/enough": "value"}, "Nested"
    assert flatten({"empty": {}}) == {"empty": ""}, "Empty value"
    assert flatten({
        "name": {
            "first": "One",
            "last": "Drone"
        },
        "job": "scout",
        "recent": {},
        "additional": {
            "place": {
                "zone": "1",
                "cell": "2"
            }
        },
    }) == {
        "name/first": "One",
        "name/last": "Drone",
        "job": "scout",
        "recent": "",
        "additional/place/zone": "1",
        "additional/place/cell": "2",
    }
    print("OK")
