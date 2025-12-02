current_number = 50
zeros = 0


with open('input', 'r') as f:
    for line in f:
        line = line.strip()

        magnitude = int(line.strip('LR'))

        if line.startswith('L'):
            magnitude *= -1

        rotations = abs(int((current_number + magnitude) / 100))

        if current_number + magnitude < 0 and not current_number == 0:
            rotations += 1

        current_number = (current_number + magnitude) % 100

        if current_number == 0 and rotations > 0:
            rotations -= 1

        zeros += rotations

        if current_number == 0:
            zeros += 1


print(zeros)
