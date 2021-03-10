#https://programmers.co.kr/learn/courses/30/lessons/43105

def solution(triangle):
    answer = 0
    if(len(triangle) == 1):
        return triangle[0][0]
    if(len(triangle) == 2):
        temp_list = []
        for i in range(len(triangle) - 1):

            for j in range(len(triangle[i])):

                add_list = [triangle[i][j] + triangle[i+1][j] , triangle[i][j] + triangle[i+1][j+1]]

        add_list = sorted(add_list)
        return add_list[-1]

    '''
    길이 3 이상
    '''
    triangle[1] = [triangle[0][0] + triangle[1][0],triangle[0][0] + triangle[1][1]] # 더해준 경로값, len = 2



    for i in range(1, len(triangle) - 1): # 높이

        update = []
        update.append(triangle[i][0] + triangle[i+1][0]) # 첫번째 줄
        temp_weight = (triangle[i][0] + triangle[i+1][1])
        for j in range(1,len(triangle[i]) - 1): # 윗 부분의 1번부터 마지막줄 이전까지
            new_weight = triangle[i][j] + triangle[i+1][j]
            if(temp_weight <= new_weight):
                update.append(new_weight)
                temp_weight = new_weight
            else:
                update.append(temp_weight)
            temp_weight = triangle[i][j] + triangle[i+1][j+1]
        # 루프가 끝나고 마지막
        new_weight = triangle[i][len(triangle[i]) - 1] + triangle[i + 1][len(triangle[i]) - 1]
        if (temp_weight <= new_weight):
            update.append(new_weight)
            temp_weight = new_weight
        else:
            update.append(temp_weight)
        update.append(triangle[i][len(triangle[i]) - 1] + triangle[i + 1][len(triangle[i])])
        #print(update)
        triangle[i + 1] = update


    answer = sorted(triangle[-1])
    return answer[-1]


'''
def solution(triangle):
    dp = []
    for t in range(1, len(triangle)):
        for i in range(t+1):
            if i == 0:
                triangle[t][0] += triangle[t-1][0]
            elif i == t:
                triangle[t][-1] += triangle[t-1][-1]
            else:
                triangle[t][i] += max(triangle[t-1][i-1], triangle[t-1][i])
    return max(triangle[-1])
    
모범코드...... 훨씬 짧다


'''