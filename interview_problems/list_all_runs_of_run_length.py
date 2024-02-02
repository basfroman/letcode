def solution(values, run_length):
    result = []

    for i in range(len(values) - run_length + 1):
        # get the start and end of the range based on run_length
        start, end = values[i], values[i + run_length - 1]
        # determine the proper direction of increasing or decreasing the number in the range
        start, end, direction = (start, end, 1) if end > start else (end, start, -1)

        # check if the current range on the value is the same expected one based on direction
        if end - start == run_length - 1 and values[i:i + run_length] == list(range(start, end + 1))[::direction]:
            result.append(i)

    return result


if __name__ == '__main__':
    vals = [1, 11, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
    run_l = 3
    assert solution(vals, run_l) == [4, 6, 7]

    vals = [1, 2, 3, 5, 10, 9, 8, 9, 10, 11, 7, 8, 7]
    run_l = 3
    assert solution(vals, run_l) == [0, 4, 6, 7]

    vals = [10, 9, 8, 7, 8, 9, 10]
    run_l = 2
    assert solution(vals, run_l) == [0, 1, 2, 3, 4, 5]


