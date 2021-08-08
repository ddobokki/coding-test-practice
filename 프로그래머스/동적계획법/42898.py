#https://programmers.co.kr/learn/courses/30/lessons/42898

def make_2d_arr(m,n,puddles):
    # arr = []
    # for row in range(n):
    #     arr.append([0]*m)
    arr = [[0 for col in range(m)] for row in range(n)]
    if(len(puddles) >0):
        for p in puddles:
            arr[p[1]-1][p[0]-1] = -1 ### 배열 위치 잘 확인하자
    return arr


def solution(m, n, puddles):
    arr = make_2d_arr(m, n, puddles)

    for i in range(len(arr[0])):
        if (arr[0][i] != -1):
            arr[0][i] = 1
        else:
            break

    for j in range(len(arr)):
        if (arr[j][0] != -1):
            arr[j][0] = 1
        else:
            break

    for i in range(1, len(arr)):
        for j in range(1, len(arr[i])):
            if (arr[i][j] == -1):
                continue
            up = arr[i - 1][j]
            left = arr[i][j - 1]

            if (up != -1 and left != -1):
                arr[i][j] = up + left
            elif (up == -1 and left != -1):
                arr[i][j] = left
            elif (left == -1 and up != -1):
                arr[i][j] = up
            else:
                arr[i][j] = -1

        answer = arr[-1][-1] % 1000000007
    return answer

# print(solution(2, 2, []), 2)
# print(solution(3, 3, []), 6)
# print(solution(3, 3, [[2, 2]]), 2)
# print(solution(3, 3, [[2, 3]]), 3)
# print(solution(3, 3, [[1, 3]]), 5)
# print(solution(3, 3, [[1, 3], [3, 1]]), 4)
# print(solution(3, 3, [[1, 3], [3, 1], [2, 3]]), 2)
# print(solution(3, 3, [[1, 3], [3, 1], [2, 3], [2, 1]]), 1)
#test = make_2d_arr(7,4 ,[[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]])

print(solution(7, 4, [[2, 1], [2, 2], [2, 3], [4, 2], [4, 3], [4, 4], [6, 2], [6, 3]]), 0) # 이 값이 잘 나오면 테스트1, 테스트9 통과, 위로 가면 안됨
print(solution(4, 4, [[3, 2], [2, 4]]), 7)
print(solution(100, 100, []), 690285631)