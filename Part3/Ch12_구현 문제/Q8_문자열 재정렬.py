words = input()

arr = []
cal = 0
for word in words:
    if word.isalpha():
        arr.append(word)
    else:
        cal += int(word)

print(''.join(sorted(arr))+str(cal))