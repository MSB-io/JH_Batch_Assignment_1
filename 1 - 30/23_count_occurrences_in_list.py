lst = input("Enter numbers separated by spaces: ").split()
lst = [int(num) for num in lst]
num_to_count = int(input("Enter a number to count: "))
print(f"Occurrences: {lst.count(num_to_count)}")