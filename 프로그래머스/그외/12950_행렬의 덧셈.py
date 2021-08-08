def solution(arr1, arr2):
    answer = []
    for row1,row2 in zip(arr1,arr2):
        add = []
        for col1,col2 in zip(row1,row2):
            add.append(col1+col2)
        answer.append(add)
    return answer

solution([[1,2],[2,3]],	[[3,4],[5,6]])