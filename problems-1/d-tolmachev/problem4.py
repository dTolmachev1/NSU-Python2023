#!/usr/bin/env python3

quantities: list[str] = ['no', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']    # Numbers as strings

# Pluralize word if necessary
def bottle(i: int) -> str:
    return 'bottle' + ('s' if i != 1 else '')

# Used as entrypoint
if __name__ == '__main__':
    for i in range(10, 0, -1):
        print(f'{quantities[i].capitalize()} green {bottle(i)} hanging on the wall,\n' * 2, end = '')
        if i == 1:
            print('If that one green bottle should accidentally fall,')
        else:
            print('And if one green bottle should accidentally fall,')
        print(f'There’ll be {quantities[i - 1]} green {bottle(i - 1)} hanging on the wall.')
