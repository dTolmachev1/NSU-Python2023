def solve_with_recursion(number: int) -> str:
	if number == 1:
		return '1'
	return str(number) + ' -> ' + solve_with_recursion(
		number // 2 if number % 2 == 0 else number * 3 + 1)


def solve_with_iteration(number: int) -> str:
	result = str(number)
	while number != 1:
		number = number // 2 if number % 2 == 0 else number * 3 + 1
		result += ' -> ' + str(number)
	return result


if __name__ == '__main__':
	print("Please, print a number.")
	number = int(input())
	print(solve_with_recursion(number))
	print(solve_with_iteration(number))
