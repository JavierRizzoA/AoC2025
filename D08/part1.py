import math

def distance(box_a, box_b):
    return math.sqrt(math.pow(box_a['x'] - box_b['x'], 2) + math.pow(box_a['y'] - box_b['y'], 2) + math.pow(box_a['z'] - box_b['z'], 2))


boxes = []
with open('input', 'r') as f:
    for line in f:
        line = line.strip()
        x, y, z = line.split(',')
        boxes.append({'x': int(x), 'y': int(y), 'z': int(z), 'circuit': None})


distances = []
for a in range(len(boxes) - 1):
    for b in range(a + 1, len(boxes)):
        distances.append((a, b, distance(boxes[a], boxes[b])))

distances.sort(key=lambda x: x[2])


circuit_index = 0
for i in range(1000):
    connection = distances[i]
    if boxes[connection[0]]['circuit'] == None and boxes[connection[1]]['circuit'] == None:
        boxes[connection[0]]['circuit'] = circuit_index
        boxes[connection[1]]['circuit'] = circuit_index
        circuit_index += 1
    if not boxes[connection[0]]['circuit'] == None and boxes[connection[1]]['circuit'] == None:
        boxes[connection[1]]['circuit'] = boxes[connection[0]]['circuit']
    if boxes[connection[0]]['circuit'] == None and not boxes[connection[1]]['circuit'] == None:
        boxes[connection[0]]['circuit'] = boxes[connection[1]]['circuit']
    else:
        index1 = boxes[connection[0]]['circuit']
        index2 = boxes[connection[1]]['circuit']
        for box in boxes:
            if box['circuit'] == index1 or box['circuit'] == index2:
                box['circuit'] = circuit_index;
        circuit_index += 1


circuit_sizes = {}
for box in boxes:
    circuit = box['circuit']
    if circuit is not None:
        if circuit in circuit_sizes.keys():
            circuit_sizes[circuit] += 1
        else:
            circuit_sizes[circuit] = 1

circuit_sizes = list(circuit_sizes.values())
circuit_sizes.sort(reverse=True)

print(circuit_sizes[0] * circuit_sizes[1] * circuit_sizes[2])
