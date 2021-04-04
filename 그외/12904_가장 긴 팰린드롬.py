def solution(s):
    if len(s) == 1:
        return 1
    palin_list = []
    for i,char_s in enumerate(s):
        start = i
        palindrome_len = 0
        for j in range(1,len(s)):
            if char_s == s[i]:
                if s[start:j+1] == s[start:j+1][::-1]:
                    palindrome_len = len(s[start:j+1])
            palin_list.append(palindrome_len)

    return max(palin_list)


print(5//2)
"""
당연하게도 시간초과
li = []

def is_palindrome(s):
    if len(s) == 1:
        return 0
    if s == s[::-1]:
        return li.append(len(s))
    else:
        is_palindrome(s[0:len(s) - 1])
        is_palindrome(s[1:len(s)])
        is_palindrome(s[1:len(s)-1])


def solution(s):
    is_palindrome(s)

    return max(li)
    
    
    """

print(solution("aa"))