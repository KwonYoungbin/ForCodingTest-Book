from collections import deque

n, m = map(int, input().split())
weight = deque(list(map(int, input().split())))
result = 0

while weight:
    now = weight.popleft()
    if weight:
        result += len(weight) - weight.count(now)

print(result)