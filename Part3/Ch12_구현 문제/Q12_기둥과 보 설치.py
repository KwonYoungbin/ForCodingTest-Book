# 현재 answer이 가능한 경우인지 확인
def chk_possible(arr):
    for x, y, a in arr:
        if a == 0:  # 기둥 설치 조건 확인
            if y == 0 or [x, y - 1, 0] in arr or [x - 1, y, 1] in arr or [x, y, 1] in arr:
                continue
            return False
        else:  # 보 설치 조건 확인
            if ([x, y - 1, 0] in arr) or ([x + 1, y - 1, 0] in arr) or ([x - 1, y, 1] in arr and [x + 1, y, 1] in arr):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for x, y, a, b in build_frame:
        if b == 1:  # 설치하는 경우
            answer.append([x, y, a])  # 우선 추가한 뒤, 조건에 부합하지 않으면 다시 삭제
            if not chk_possible(answer):
                answer.remove([x, y, a])
        else:  # 삭제하는 경우
            answer.remove([x, y, a])  # 우선 삭제한 뒤, 조건에 부합하지 않으면 다시 추가
            if not chk_possible(answer):
                answer.append([x, y, a])

    answer = sorted(answer, key=lambda x: (x[0], x[1], x[2]))

    return answer