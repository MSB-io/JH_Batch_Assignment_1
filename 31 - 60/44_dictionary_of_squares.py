def dictionary_of_squares(n):
    return {x: x**2 for x in range(1, n + 1)}

print(dictionary_of_squares(5))  # Example: {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}