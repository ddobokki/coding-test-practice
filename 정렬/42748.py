#https://programmers.co.kr/learn/courses/30/lessons/42748
def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        #print(array)
        temp_array = array[commands[i][0]-1: commands[i][1]]
        temp_array.sort()
        #print(i, temp_array)
        answer.append(temp_array[commands[i][2]-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4],[[2, 5, 3], [4, 4, 1], [1, 7, 3]]))

b = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(len(b))
print(b[2][0])