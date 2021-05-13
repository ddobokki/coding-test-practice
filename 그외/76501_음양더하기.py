def solution(absolutes, signs):
    ans = 0
    for n, sign in zip(absolutes, signs):
        if sign:
            ans += n
        else:
            ans -= n


    return ans