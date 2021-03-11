#https://programmers.co.kr/learn/courses/30/lessons/42840

def solution(answers):
    answer = []

    num_test = len(answers)

    pattern1 = [1, 2, 3, 4, 5]
    pattern2 = [2, 1, 2, 3, 2, 4, 2, 5]
    pattern3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    answer_sheet1 = (pattern1 * (int(num_test / len(pattern1)) + 1))[0:num_test]
    answer_sheet2 = (pattern2 * (int(num_test / len(pattern2)) + 1))[0:num_test]
    answer_sheet3 = (pattern3 * (int(num_test / len(pattern3)) + 1))[0:num_test]

    #print(answer_sheet1)
    #print(answer_sheet2)
    #print(answer_sheet3)

    count1 = 0
    count2 = 0
    count3 = 0
    for n in range(num_test):
        right = answers[n]
        if right == answer_sheet1[n]:
            count1 += 1
        if right == answer_sheet2[n]:
            count2 += 1
        if right == answer_sheet3[n]:
            count3 += 1
    scores = [count1, count2, count3]
    max_socre = max(scores)

    i = 1
    for score in scores:
        if score == max_socre:
            answer.append(i)
        i += 1
    return answer

'''
    for idx, s in enumerate(score):
        if s == max(score):
            result.append(idx+1)
            
    다른 사람의 일부, 인덱스와 값을 알고 있을땐 enumberate를 사용하면 좀더 깔끔해진다.

'''
