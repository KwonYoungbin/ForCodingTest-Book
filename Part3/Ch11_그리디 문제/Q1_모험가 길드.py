n = int(input())
arr = list(map(int, input().split()))
arr.sort()
result = 0

count = 0
data_check = []

for v in arr:
    count += 1
    data_check.append(v)
    if count >= v:
        result += 1
        count = 0
        print(data_check, end=' ')
        data_check = []

print(result)