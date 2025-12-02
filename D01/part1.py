current_number = 50
zeros = 0

with open('input', 'r') as f:
    for line in f:
        line = line.strip()
        magnitude = int(line.strip('LR'))
        if line.startswith('L'):
            magnitude *= -1
        current_number += magnitude

        while current_number > 99:
            current_number -= 100

        while current_number < 0:
            current_number += 100

        if current_number == 0:
            zeros += 1

print(zeros)
