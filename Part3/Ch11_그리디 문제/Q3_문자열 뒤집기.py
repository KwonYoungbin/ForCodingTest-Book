num = input()

while '00' in num:
    num = num.replace('00','0',-1)

while '11' in num:
    num = num.replace('11','1',-1)

cnt_0 = num.count('0')
cnt_1 = num.count('1')

print(min(cnt_0, cnt_1)) if cnt_0 != 0 and cnt_1 != 0 else print(1)