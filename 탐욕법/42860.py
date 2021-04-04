#https://programmers.co.kr/learn/courses/30/lessons/42860

def number_of_operations(target,forword,reverse):

    for_num_oper = forword.index(target)
    rev_num_oper = reverse.index(target) + 1

    return [for_num_oper,rev_num_oper]

def number_of_horizontal(name):
    idx = 0
    name_li = list(name)
    num = 0
    name_li[idx] = 'A'
    while True:

        for i in range(1,len(name_li)):
            if(name_li[idx + i] != 'A'):
                name_li[idx + i] = 'A'
                num += i
                idx = idx + i
                break
            if(name_li[idx - i] != 'A'):
                name_li[idx - i] = 'A'
                num += i
                idx = idx - i
                break

        if(all(list(map(lambda x:x == 'A',name_li)))):
            break
    return num

def solution(name):
    forword_alphabet = []
    reverse_alphabet = []
    for i in range(ord('A'), ord('Z') + 1):
        forword_alphabet.append(chr(i))
        reverse_alphabet.append(chr(ord('Z') + ord('A') - i))


    answer = number_of_horizontal(name)

    for n in name:
        answer += min(number_of_operations(n,forword_alphabet,reverse_alphabet))
    return answer

'''
탐욕법:
작은 최선의 값을 더하는게 최대의 최선이 값이 되는것

'''

print(number_of_horizontal("BBBAAAAAAAAAAB"))