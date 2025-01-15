minimum, maximum = lst[0], lst[0]
for num in lst:
    if num < minimum:
        minimum = num
    if num > maximum:
        maximum = num
print(f"Min: {minimum}, Max: {maximum}")