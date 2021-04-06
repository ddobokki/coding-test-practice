def solution(s):
    answer = ''
    s = s.lower()
    words = s.split()
    change_w = []
    for word in words:
        if word[0].isalpha():
            change_w.append(word[0].upper() + word[1:])
        else:
            change_w.append(word)
    s_li = list(s)
    idx = 0
    i = 0
    while idx < len(s):
        if s[idx] == " ":
            answer += s[idx]
            idx += 1
        else:
            answer += change_w[i]
            idx += len(change_w[i])
            i += 1

    return answer

print(solution("3people    unFollowed me"))

print(solution(" a bc"))
a = " a bc"
print(a.split(' '))