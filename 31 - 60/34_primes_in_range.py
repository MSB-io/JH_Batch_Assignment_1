def primes_in_range(start, end):
    return [num for num in range(start, end + 1) if is_prime(num)]

print(primes_in_range(10, 50))  # Example: List of primes between 10 and 50