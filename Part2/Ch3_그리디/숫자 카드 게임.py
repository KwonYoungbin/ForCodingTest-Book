import sys

n, m = map(int, sys.stdin.readline().split())
result = 0

for _ in range(n):
    result = max(result, min(list(map(int, sys.stdin.readline().split()))))

print(result)