#https://programmers.co.kr/learn/courses/30/lessons/42883
def solution(number, k):
    collected = []

    for (i, num) in enumerate(number):
        print(collected, k)
        while collected and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1

        if k == 0:
            collected += number[i:]
            break

        collected.append(num)

    collected = collected[:-k] if k > 0 else collected
    answer = "".join(collected)
    return answer

print(solution("4177852841",4))

