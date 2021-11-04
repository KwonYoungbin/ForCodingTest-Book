n = int(input())
arr = list(map(int, input().split()))
dp = [0] * 101

for i in range(1, n+1):
    dp[i] = arr[i-1]
    if i-2 >= 0:
        dp[i] = max(dp[i-2]+dp[i], dp[i-1])
print(dp[n])