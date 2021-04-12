import itertools
def solution(expression:str):
    answer = []
    expression_list = []

    cur_str = ""
    for i in range(len(expression)): # 수식을 리스트로 바꿈
        if expression[i] == '+' or expression[i] == '-' or expression[i] == '*':
            expression_list.append(cur_str)
            cur_str = ""
            expression_list.append(expression[i])
        else:
            cur_str += expression[i]
    expression_list.append(cur_str)

    oper = set() # 수식에 있는 연산자 추출
    for ex in expression:
        if not ex.isdigit():
            oper.add(ex)

    oper_priority_list = list(itertools.permutations(oper,len(oper))) # 연산자 우선순위를 정함 높을수록 인덱스 낮음

    for oper_priority in oper_priority_list: # 각 연산에 대해 모두 계산

        temp_ex = expression_list.copy() # 리스트로 바꾼 수식을 카피해서 넘겨줌

        for op in oper_priority: # 바꾼 연산자 우선순위에 대하여 계산
            temp_cal = [] # ex) *,+,- 의 경우 0> *를 계산한 값을 먼저 저장, 그후 다음을 계산
            is_cal = False # cal에 숫자를 넣어줄 플래그
            for idx, ex in enumerate(temp_ex):
                if ex == op:
                    temp_cal.append(str(int(eval(temp_cal.pop() + temp_ex[idx] + temp_ex[idx+1]))))
                    is_cal = True
                else:
                    if is_cal:
                        is_cal = False
                        continue
                    else:
                        temp_cal.append(ex)

            temp_ex = temp_cal
        answer.append(abs(int(temp_cal[0])))


    return max(answer)

solution("100-200*300-500+20")