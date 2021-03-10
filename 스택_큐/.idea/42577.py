#https://programmers.co.kr/learn/courses/30/lessons/42577
def find_index(sorted_phone_book):
    len_list = list(map(lambda x: len(x),sorted_phone_book))
    index = 0
    return_list = []
    for i in len_list[1:]:
        if(len_list[index] != i):
            return_list.append(index+1)
        index = index+1
    return return_list
def solution(phone_book):
    answer = True
    phone_book = sorted(phone_book,key=len) #정렬, 문자열 길이순
    index_list = find_index(phone_book) # 정렬된 리스트로부터 길이가 달라지는 지점의 인덱스들을 찾는다
    f_i = 0 # 시작 인덱스
    for l_i in index_list:
        slice_len = len(phone_book[f_i:l_i][0]) # 접두사의 문자열 길이로 긴 전화번호를 앞에서 부터 잘라준다.
        short_phone_nums = set(phone_book[f_i:l_i])
        long_phone_nums = set(list(map(lambda x:x[0:slice_len],phone_book[l_i:])))
        if(len(short_phone_nums.intersection(long_phone_nums)) != 0): # 짧은 번호와, 자른 긴 번호의 교집합이 있으면 False가 됨
            answer = False
        f_i = l_i
    return answer



'''
처음의 나의 풀이
문제점 
[11, 222, 223]의 경우 True가 나와야 하는데 
첫 루프 11, 22, 22가 되어버려 다른 값을 도출

def find_phone_num_len(phone_book):
    return_list =list(set(map(lambda x:len(x),phone_book)))
    return_list.sort()
    return return_list

def solution(phone_book):
    phone_book.sort()
    phone_book_set_len = len(set(phone_book))
    phone_book_len = find_phone_num_len(phone_book)
    answer = True
    for i in phone_book_len:
        temp = list(map(lambda x: x[0:i], phone_book))
        slice_phone_book_len = len(set(temp))
        #print(list(map(lambda x: x[0:i], phone_book)))
        #print(set(temp))
        if (phone_book_set_len != slice_phone_book_len):  # 길이가 달라지면 접두가 있다는것
            answer = False
            break

    return answer
'''
test = []


test =['4281668', '3622797', '944037', '3270990', '6430984', '7465740',
 '4381264', '6967901', '1125267', '2368755', '8807073', '2653112',
 '9072068', '9669370', '5899392', '6963717', '49', '6186770', '3235612',
 '6177142', '2646632', '3141931', '5379326', '9558737', '9103423', '8591201',
 '2109266', '6200047', '6610732', '7851861', '1498103', '4631826', '3424845',
 '6691255', '8617626', '7520767', '4868889', '9555981', '1611662', '3968265']


#print(find_index(test))
#print(test)
#print(solution(["12","123","1235","567","88"]))
#print(test)
#print(solution(test))
#a = set(['a','b','c'])
