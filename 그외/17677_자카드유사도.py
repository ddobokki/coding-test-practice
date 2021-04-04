def get_set(s):
    s = s.lower()
    return_set = []
    for i in range(len(s) - 1):
        temp_s = ""
        for j in range(2):
            if ord('a') <= ord(s[i + j]) <= ord('z'):
                temp_s += s[i + j]
        if len(temp_s) == 2:
            return_set.append(temp_s)

    return return_set


def get_inter(s11, s22):
    inter_set = []
    s1 = s11.copy()
    s2 = s22.copy()
    for i in range(len(s1)):
        s = s1.pop()

        for j in range(len(s2)):
            if s == s2[j]:
                s2.pop(j)
                inter_set.append(s)
                break
    return inter_set


def get_union(s1, s2):
    inter = get_inter(s1, s2)
    diff1 = get_diff(s1, inter)
    diff2 = get_diff(s2, inter)
    return inter + diff1 + diff2


def get_diff(s1, s2):
    s11 = s1.copy()

    for s in s2:

        for j in range(len(s11)):
            if s == s11[j]:
                s11.pop(j)
                break
    return s11


def solution(str1, str2):
    if str1.lower() == str2.lower():
        return 65536

    set1 = get_set(str1)
    set2 = get_set(str2)

    inter = get_inter(set1, set2)
    union = get_union(set1, set2)

    answer = len(inter) / len(union)

    return int(answer * 65536)

a = [ 1,2,3]
b = [2,3,4]

print(set(a) | set(b))
