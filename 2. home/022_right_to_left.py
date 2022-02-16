def left_join(phrases: tuple) -> str:
    """
    Join strings and replace "right" to "left"
    """
    result = []
    for phrase in phrases:
        result.append(phrase.replace('right', 'left'))
    return ','.join(result)


if __name__ == '__main__':

    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok"
    assert left_join(("brightness wright",)) == "bleftness wleft"
    assert left_join(("enough", "jokes")) == "enough,jokes"

    print("OK")
