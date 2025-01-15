def second_largest(lst):
    unique_sorted = sorted(set(lst), reverse=True)
    return unique_sorted[1]

print(second_largest([4, 1, 7, 3, 7, 8]))  # Example: 7