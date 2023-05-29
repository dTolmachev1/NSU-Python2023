def cum_sum(seq: list[int]) -> list[int]:
    res = [0]
    for i in range(len(seq)):
        res.append(res[i] + seq[i])
    return res


if __name__ == '__main__':
    tests = [[1, 2, 3], [], [1]*1000, [-1, -2, -3]]
    corr = [[0, 1, 3, 6], [0], [i for i in range(1001)], [0, -1, -3, -6]]
    for k in range(len(tests)):
        assert cum_sum(tests[k]) == corr[k]
