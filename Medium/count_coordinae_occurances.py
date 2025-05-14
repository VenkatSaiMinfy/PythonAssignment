def count_coordinate_occurrences(coords):
    count = {}
    for coord in coords:
        count[coord] = count.get(coord, 0) + 1
    return count

n = int(input("n: "))
coords = []

for _ in range(n):
    x, y = map(int, input().split())
    coords.append((x, y))

print(count_coordinate_occurrences(coords))
