import copy
def rotation(x1,y1,x2,y2,a):

    temp = []
    for i in range(y2 - y1 + 1):
        #print(a[y1+i][x1:x2+1])
        temp.append(a[y1+i][x1:x2+1])
    min_n = a[y1][x1]
    for i in range(x2 - x1):
        #print(a[y1][x1+i+1], temp[y1][x1+i])
        a[y1][x1+i+1] = temp[0][i]
        min_n = min(min_n,a[y1][x1+i+1])

    for i in range(y2 - y1):
        a[y1+i+1][x2] = temp[i][len(temp[0]) - 1]
        min_n = min(min_n, a[y1+i+1][x2])

    for i in range(x2 - x1):
        #print(temp[len(temp)-1][len(temp[0])-1 - i])
        a[y2][x2 - i - 1] = temp[len(temp)-1][len(temp[0])-1 - i]
        min_n = min(min_n, a[y2][x2 - i - 1])


    for i in range(y2 - y1):
        a[y2 - i - 1][x1] = temp[len(temp)-1 - i][0]
        min_n = min(min_n, a[y2 - i - 1][x1])


    return min_n

def solution(rows, columns, queries):
    answer = []
    arr = []
    num = 1
    for i in range(rows):
        temp = []
        for j in range(columns):
            temp.append(num)
            num += 1
        arr.append(temp)

    for q in queries:
        y1,x1,y2,x2 = q
        answer.append(rotation(x1-1,y1-1,x2-1,y2-1,arr))

    print(answer)
    return answer
solution(6,	6,	[[2,2,5,4],[3,3,6,6],[5,1,6,3]])
solution(3,	3,	[[1,1,2,2],[1,2,2,3],[2,1,3,2],[2,2,3,3]])
#solution(6	6	[[2,2,5,4],[3,3,6,6],[5,1,6,3]])
