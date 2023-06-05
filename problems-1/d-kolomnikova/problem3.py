import logging


def int_input() -> int:
    inp = input("Enter positive integer: ")
    n = int(inp)
    if n < 1:
        raise ValueError
    return n


if __name__ == "__main__":
    try:
        x = int_input()
    except Exception as e:
        logging.error(str(e))
        logging.error("Invalid input: positive integer expected")
        exit()
    while x != 1:
        print(x, end=' -> ')
        x = int(x / 2 if x % 2 == 0 else 3 * x + 1)
    print(x)
