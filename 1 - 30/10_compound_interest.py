P = float(input("Principal amount: "))
R = float(input("Interest rate: "))
T = float(input("Time in years: "))
n = int(input("Times compounded per year: "))
CI = P * (1 + R / (100 * n)) ** (n * T) - P
print(f"Compound Interest: {CI:.2f}")