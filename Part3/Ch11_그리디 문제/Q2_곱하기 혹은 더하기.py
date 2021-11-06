words = list(map(int,input()))
result = words[0]

for i in range(1, len(words)):
    if result <= 1 or words[i] <= 1:
        result += words[i]
    else:
        result *= words[i]
print(result)