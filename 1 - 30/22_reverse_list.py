lst = [1, 2, 3, 4, 5]  # example list, modify as needed
for i in range(len(lst) // 2):
    lst[i], lst[-i-1] = lst[-i-1], lst[i]
print(f"Reversed list: {lst}")