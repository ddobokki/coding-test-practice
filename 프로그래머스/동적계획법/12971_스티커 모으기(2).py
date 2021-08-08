# https://programmers.co.kr/learn/courses/30/lessons/12971

def solution(sticker):
    if len(sticker) <= 3:
        return max(sticker)

    add_sticker1 = [0] * len(sticker)

    add_sticker1[0] = sticker[0]
    add_sticker1[1] = max(sticker[0],sticker[1])

    for i in range(2, len(sticker) - 1):
        add_sticker1[i] = max(add_sticker1[i - 1], sticker[i] + add_sticker1[i - 2])

    add_sticker2 = [0] * len(sticker)

    add_sticker2[0] = 0
    add_sticker2[1] = sticker[1]

    for i in range(2, len(sticker)):
        add_sticker2[i] = max(add_sticker2[i - 1], sticker[i] + add_sticker2[i - 2])
    return max(max(add_sticker1), max(add_sticker2))


s = [14, 6, 5, 11, 3, 9, 2, 10]
s = [1,2]
print(solution([14, 6, 5, 11, 3, 9, 2, 10]))
