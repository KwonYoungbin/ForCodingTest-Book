import sys
from itertools import combinations

INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())
cities = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

chicken = []
house = []

for row in range(n):
    for col in range(n):
        if cities[row][col] == 2:
            chicken.append((row, col))
        elif cities[row][col] == 1:
            house.append((row, col))

combi = combinations(chicken, m)
result = INF

for case in combi:
    cal = 0
    for h in house:
        now = INF
        for c in case:
            now = min(now, (abs(h[0]-c[0]) + abs(h[1]-c[1])))
        cal += now
    result = min(result, cal)
print(result)