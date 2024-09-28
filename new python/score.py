possibilities = []

for a in range(5, 10):
    for b in range(5, 10):
        for c in range(1, 10):
            result = (a + b) * 2 + c
            if result == 41.75:
                possibilities.append((a, b, c))

print(possibilities)