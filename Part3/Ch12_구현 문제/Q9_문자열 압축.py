# 원리는 이해했으나, 구현에 어려움이 있었음.
# 복습할 필요가 있음.

def solution(s):
    answer = []

    if len(s) == 1:
        return 1

    for i in range(1, len(s) // 2 + 1):
        result = ''
        count = 1
        temp = s[:i]
        for j in range(i, len(s), i):
            if s[j:j + i] == temp:
                count += 1
            else:
                if count != 1:
                    result += str(count) + temp
                else:
                    result += temp
                temp = s[j:j + i]
                count = 1
        if count != 1:
            result += str(count) + temp
        else:
            result += temp
        answer.append(len(result))

    return min(answer)

# Ver.2

# def solution(s):
#     answer = len(s)
#
#     if len(s) == 1:
#         return 1
#
#     for i in range(1, len(s) // 2 + 1):
#         result = ''
#         count = 1
#         temp = s[:i]
#         for j in range(i, len(s), i):
#             if s[j:j + i] == temp:
#                 count += 1
#             else:
#                 if count != 1:
#                     result += str(count) + temp
#                 else:
#                     result += temp
#                 temp = s[j:j + i]
#                 count = 1
#         if count != 1:
#             result += str(count) + temp
#         else:
#             result += temp
#         answer = min(answer, len(result))
#
#     return answer