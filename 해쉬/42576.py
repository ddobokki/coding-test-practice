#https://programmers.co.kr/learn/courses/30/lessons/42576

def count_participant(participant):
    p_dict = dict()
    
    for p in participant:
        if not p in p_dict:
            p_dict[p] = 1
        else:
            p_dict[p] = p_dict[p] + 1
    return p_dict
def count_completion(p_dict,completion):
    
    for c in completion:
        p_dict[c] = p_dict[c] - 1
    return p_dict

def find(p_dict):
    list_values = list(p_dict.values())
    list_keys = list(p_dict.keys())
    
    
    return list_keys[list_values.index(1)]

def solution(participant, completion):
    p = count_participant(participant)
    pp = count_completion(p,completion)
    answer = find(pp)
    return answer
