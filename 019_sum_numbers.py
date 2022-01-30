def sum_numbers(text: str) -> int:
    words = text.split()
    total = 0
    for word in words:
        if word.isnumeric():
            total += int(word)
    return total


if __name__ == "__main__":

    assert sum_numbers("hi") == 0
    assert sum_numbers("who is 1st here") == 0
    assert sum_numbers("my numbers is 2") == 2
    assert (
        sum_numbers(
            "This picture is an oil on canvas "
            "painting by Danish artist Anna "
            "Petersen between 1845 and 1910 year"
        ) == 3755
    )
    assert sum_numbers("5 plus 6 is") == 11
    assert sum_numbers("") == 0

    print("OK")
