from math import sqrt


def decompose(x: int) -> [[int]]:
    res = {}
    i = 2
    bord = int(sqrt(abs(x)))
    while i <= bord:
        if x % i == 0:
            res.update({i: res.setdefault(i, 0) + 1})
            x /= i
        else:
            i += 1
    return [[i, j] for (i, j) in zip(res.keys(), res.values())]


if __name__ == "__main__":
    tests = [5, 12, 100]
    corr = [[], [[2, 2], [3, 1]], [[2, 2], [5, 2]]]
    for k in range(len(tests)):
        assert decompose(tests[k]) == corr[k]
