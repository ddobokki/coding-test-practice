def is_star(a):
    temp_a = []
    for i in range(len(a)//2):
        temp_a.append({a[2 * i], a[2 * i + 1]})

    aa = temp_a[0]
    for i in range(1,len(temp_a)):
        aa = aa.intersection(temp_a[i])
    if len(aa) == 0:
        return False

    for i in range(len(a)//2):
        if a[2*i] == a[2*i+1]:
            return False
    return True
def solution(a):
    answer = -1

    set_a = list(set(a))
    # 센터를 포함한 부분수열들을 만듬
    for center in set_a:
        center_idx = []
        for i in range(len(a)):
            if a[i] == center:
                center_idx.append(i)
        start_idx = 0
        star = []
        for i in center_idx:

            for j in range(i,len(a)):
                if a[j] != center:
                    start_idx = j + 1
                    if j > i:
                        star.append(center)
                        star.append(a[j])
                    else :
                        star.append(a[j])
                        star.append(center)
                    break
        print(star)

    return answer

print(solution([5,2,3,3,5,3]))
'''
def is_star(a):
    temp_a = []
    for i in range(len(a)//2):
        temp_a.append({a[2 * i], a[2 * i + 1]})

    aa = temp_a[0]
    for i in range(1,len(temp_a)):
        aa = aa.intersection(temp_a[i])
    if len(aa) == 0:
        return False

    for i in range(len(a)//2):
        if a[2*i] == a[2*i+1]:
            return False
    return True

def solution(a):
    answer = -1

    if len(a) % 2 == 0:
        start = len(a)
    else:
        start = len(a) - 1

    for i in range(start,1,-2):
        add_i = list(combinations(range(len(a)),i))
        for j in add_i:
            temp = []
            for k in j:
                temp.append(a[k])
            if is_star(temp):
                return len(temp)
    return 0

시간 초과

'''