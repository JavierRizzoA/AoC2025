total_joltage = 0

with open('input', 'r') as f:
    for line in f:
        digits = [int(d) for d in line.strip()]
        d1 = max(digits[:-1])
        d1i = digits.index(d1)
        d2 = max(digits[d1i+1:])
        joltage = d1 * 10 + d2
        total_joltage += joltage

print(total_joltage)
