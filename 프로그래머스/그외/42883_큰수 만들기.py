def solution(number, k):
    number_list = []
    for i in range(len(number)):
        cur_num = int(number[i])
        if not number_list:
            number_list.append(cur_num)
        else:
            if number_list[-1] >= cur_num:
                number_list.append(cur_num)
            else:
                while number_list and k > 0:
                    #print(number_list)
                    if number_list[-1] < cur_num:
                        number_list.pop()
                        k -= 1
                    else:
                        break
                number_list.append(cur_num)
        # if len(number) - k == i + 1:
        #     break
    if k > 0:
        number_list = number_list[:-k]
    return ''.join(map(str,number_list))


#print(solution("1924", 2))
#print(solution("1231234", 3))
print(solution("2222111333", 5))
print(solution("987654321",3))
