
'''https://py.checkio.org/en/mission/largest-histogram/'''


def largest_histogram(histogram):
    cols = len(histogram)
    rows = max(histogram) + 1
    maximum = 0

    for height in range(1, rows):
        acc = 0
        for col in range(cols):
            if histogram[col] < height:
                if acc > maximum:
                    maximum = acc
                acc = 0
            else:
                acc += height
        if acc > maximum:
            maximum = acc

    return maximum


if __name__ == "__main__":
    assert largest_histogram([5]) == 5, "one is always the biggest"
    assert largest_histogram([5, 3]) == 6, "two are smallest X 2"
    assert largest_histogram([1, 1, 4, 1]) == 4, "vertical"
    assert largest_histogram([1, 1, 3, 1]) == 4, "horizontal"
    assert largest_histogram([2, 1, 4, 5, 1, 3, 3]) == 8, "complex"
    print("OK")
