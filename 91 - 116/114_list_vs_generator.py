lst = [x**2 for x in range(1000000)]  # List comprehension
gen = (x**2 for x in range(1000000))  # Generator expression

print("List size:", len(lst))
print("Generator example:", next(gen))