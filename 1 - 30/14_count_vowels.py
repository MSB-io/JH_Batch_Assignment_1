vowels = "aeiouAEIOU"
count = sum(1 for char in input("Enter a string: ") if char in vowels)
print(f"Number of vowels: {count}")