num = {0: 'no', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
       6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine', 10: 'Ten'}


def isPlural(i: int) -> str:
    return "bottles" if not i == 1 else "bottle"


if __name__ == '__main__':
    for i in range(10, 0, -1):
        hang = num[i] + " green " + isPlural(i) + " hanging on the wall,"
        print(hang + "\n" + hang)
        prefix = "And if" if not i == 1 else "If that"
        print(prefix + " one green bottle should accidentally fall,")
        print("There’ll be " + num[i - 1].lower() + " green " + isPlural(i-1) + " hanging on the wall.")
