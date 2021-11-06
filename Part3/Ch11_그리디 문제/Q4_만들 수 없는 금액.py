n = int(input())
moneys = list(map(int, input().split()))
moneys.sort()

result = 1
for money in moneys:
    if result < money:
        break
    result += money
print(result)