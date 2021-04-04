# https://programmers.co.kr/learn/courses/30/lessons/64061
from collections import deque


def solution(board, moves):
    moves = list(map(lambda x: x - 1, moves))
    basket = deque([])
    cnt = 0
    for move in moves:
        for down in range(len(board)):
            doll = board[down][move]
            if (doll != 0):
                board[down][move] = 0
                break

        if doll == 0:  # 인형이 없으면
            continue  # 다음 명령 실행

        if len(basket) == 0:
            basket.append(doll)
            continue

        if len(basket) > 0:
            doll_in_basket = basket.pop()
            if doll == doll_in_basket:
                cnt += 2
            else:
                basket.append(doll_in_basket)
                basket.append(doll)

    return cnt


board = [[0, 0, 0, 0, 0],
         [0, 0, 1, 0, 3],
         [0, 2, 5, 0, 1],
         [4, 2, 4, 4, 2],
         [3, 5, 1, 3, 1]]
moves = [1, 5, 3, 5, 1, 2, 1, 4]
moves = list(map(lambda x: x - 1, moves))
basket = deque([])
cnt = 0
for move in moves:
    for down in range(len(board)):
        doll = board[down][move]
        if(doll != 0):
            board[down][move] = 0
            break

    if doll == 0: # 인형이 없으면
        continue # 다음 명령 실행

    if len(basket) == 0:
        basket.append(doll)
        continue

    if len(basket) > 0:
        doll_in_basket = basket.pop()
        if doll == doll_in_basket:
            cnt += 2
        else:
            basket.append(doll_in_basket)
            basket.append(doll)


print(cnt)
print(basket)