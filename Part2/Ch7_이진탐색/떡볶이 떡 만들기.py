import sys

n, m = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(arr)
result = 0
while start <= end:
    mid = (start+end) // 2
    score = 0
    for item in arr:
        if mid < item:
            score += (item-mid)
    if score == m:
        result = mid
        break
    elif score > m:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)