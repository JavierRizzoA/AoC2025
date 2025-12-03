total_joltage = 0

with open('input', 'r') as f:
    for line in f:
        digits = [int(d) for d in line.strip()]

        batteries = []
        last_index = -1
        for i in range(12):
            if i == 11:
                b = max(digits[last_index+1:])
            else:
                b = max(digits[last_index+1:-(11-i)])
            last_index = digits.index(b, last_index+1)
            batteries.append(b)

        joltage = 0
        for i in range(12):
            joltage += batteries[i] * pow(10, 11-i)
        total_joltage += joltage

print(total_joltage)
