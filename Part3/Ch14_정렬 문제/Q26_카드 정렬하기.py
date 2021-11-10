import sys
import heapq

n = int(sys.stdin.readline())
q = []
result = 0

for _ in range(n):
    heapq.heappush(q, int(sys.stdin.readline()))

while len(q) >= 2:
    A = heapq.heappop(q)
    B = heapq.heappop(q)
    result += A+B
    heapq.heappush(q,A+B)

print(result)