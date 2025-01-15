base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
result = 1
for _ in range(exp):
    result *= base
print(f"{base}^{exp} = {result}")