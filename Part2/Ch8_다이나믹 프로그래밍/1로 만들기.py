x = int(input())
dp = [0] * 30

# 아직 이해가 완벽하지 않음. 다시 한번 보기.
for i in range(2, x+1):
    dp[i] = dp[i-1]+1
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)
    elif i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)
    elif i % 5 == 0:
        dp[i] = min(dp[i], dp[i // 5] + 1)
print(dp[x])