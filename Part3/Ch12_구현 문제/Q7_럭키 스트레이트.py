num = input()
left_side = map(int,num[:len(num)//2])
right_side = map(int,num[len(num)//2:])

print('LUCKY') if sum(left_side) == sum(right_side) else print('READY')