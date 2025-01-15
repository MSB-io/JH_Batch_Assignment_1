from functools import reduce

nums = [1, 2, 3, 4, 5, 6]
odd_nums = list(filter(lambda x: x % 2 != 0, nums))
sum_odds = reduce(lambda x, y: x + y, odd_nums)
print(sum_odds)