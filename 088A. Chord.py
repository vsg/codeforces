def dist(x, y):
    if x > y: x, y = y, x
    return min(y-x, x+12-y)

def solve(a, b, c):
    for x, y, z in [(a, b, c), (b, c, a), (c, a, b)]:
        d1, d2, d3 = dist(x, y), dist(y, z), dist(x, z)
        if d1 == 3 and d2 == 4 and d3 == 12-7:
            return "minor"
        if d1 == 4 and d2 == 3 and d3 == 12-7:
            return "major"
    return "strange"


a, b, c = map(lambda x: ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'B', 'H'].index(x), raw_input().split())
a, b, c = sorted([a, b, c])
print solve(a, b, c)
