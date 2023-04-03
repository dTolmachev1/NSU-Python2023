def solve(array: [int], lower_bound: int, upper_bound: int) -> [int]:
	result = list(map(lambda number: lower_bound if number < lower_bound
	else upper_bound if number > upper_bound else number, array))
	return result


if __name__ == '__main__':
	print("Please, print an array of numbers.")
	array = list(map(int, input().split()))
	print("Please, print a lower bound.")
	lower_bound = int(input())
	print("Please, print an upper bound.")
	upper_bound = int(input())
	print(solve(array, lower_bound, upper_bound))
