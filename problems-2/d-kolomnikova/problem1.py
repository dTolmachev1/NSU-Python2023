import math


def generate_pythagorean(lim: int) -> list[list[tuple[int, int, int]]]:
    pyth = [[(m*m - n*n, 2*m*n, m*m + n*n) for n in range(1, m) if m*m + n*n <= lim] for m in range(2, math.ceil(math.sqrt(lim)))]
    return pyth


if __name__ == "__main__":
    print(generate_pythagorean(20))
