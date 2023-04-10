#!/usr/bin/env python3

from typing import Iterable

# replaces all out of range sequence elements to it's boundaries
def replace_out_of_range(seq: Iterable[int], a: int, b: int) -> tuple[int]:
    return tuple(map(lambda x: check_boundaries(x, a, b), seq))    # O(n)

# Returns input iff it belongs to the specified range, or one of it's boundaries otherwise
def check_boundaries(x: int, l: int, u: int) -> int:
    if x < l:
        return l
    if x > u:
        return u
    return x

# Used as entrypoint
if __name__ == '__main__':
    print(replace_out_of_range([0, 1, 2, 3, 4], 1, 3))
