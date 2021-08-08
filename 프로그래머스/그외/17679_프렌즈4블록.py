def find_del_block(board):
    del_point = set()
    for i in range(len(board) - 1):
        for j in range(len(board[i]) - 1):

            left_up = board[i][j]
            right_up = board[i][j + 1]
            left_down = board[i + 1][j]
            right_down = board[i + 1][j + 1]

            if left_up == right_up == left_down == right_down != "":
                del_point.add((i, j))
                del_point.add((i, j + 1))
                del_point.add((i + 1, j))
                del_point.add((i + 1, j + 1))
    return list(del_point)

def down_blocks(board):
    for i in range(len(board) - 1, 0, -1):
        for j in range(len(board[i])):
            cur_bottom = board[i][j]
            if cur_bottom == "":
                up_idx = 1
                while i - up_idx > 0:
                    if board[i - up_idx][j] == "":
                        up_idx += 1
                    else:
                        break
                board[i][j],board[i-up_idx][j] = board[i-up_idx][j], board[i][j]


def solution(m, n, board):
    answer = 0
    board_arr = []
    for block in board:
        board_arr.append(list(block))

    while True:
        del_points = find_del_block(board_arr)

        if not del_points:
            break

        for y, x in del_points:
            board_arr[y][x] = ""
        down_blocks(board_arr)

    ans = 0
    for b in board_arr:
        ans += b.count("")

    return ans


#print(solution(4, 5, ["TTTANT", "RRFACC", "RRRFCC", "TRRRAA", "TTMMMF", "TMMTTJ"]))
solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"])
