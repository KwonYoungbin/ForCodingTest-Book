n, m = map(int, input().split())
moneys = [int(input()) for _ in range(n)]
dp = [0] + [99999] * 20

# 어려움......
for money in moneys:
    for i in range(money, 21):
        dp[i] = min(dp[i], dp[i-money]+1)

print(dp[m]) if dp[m] != 99999 else print(-1)