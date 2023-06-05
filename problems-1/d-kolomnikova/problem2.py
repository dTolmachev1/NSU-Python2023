import logging


def constrain(seq: [int], a: int, b: int) -> [int]:
    low = lambda x: a if x < a else x
    high = lambda x: b if x > b else x
    return list(map(high, map(low, seq)))


def parse_in() -> (int, int, list[int]):
    try:
        a = int(input("pass lower boundary: "))
        b = int(input("pass higher boundary: "))
    except Exception as e:
        raise type(e)(str(e) + "\ninteger expected for boundaries") from e

    if b < a:
        raise ValueError("higher boundary must be greater than lower, got lower boundary = {}, higher = {}".format(a, b))

    try:
        seq = list(map(int, input("pass sequence separated with space: ").split()))
    except Exception as e:
        raise type(e)(str(e) + "\ninteger sequence separated with spaces expected") from e
    return seq, a, b


if __name__ == '__main__':
    try:
        sequence, lower, higher = parse_in()
    except Exception as ex:
        logging.error(str(ex))
        exit(1)
    print(constrain(sequence, lower, higher))

