#https://programmers.co.kr/learn/courses/30/lessons/72411

'''
3문제가 시간초과가 난다. 로직은 맞는듯

'''


from itertools import combinations
import collections
def solution(orders, course):
    answer = []
    len_order = list(map(lambda x:len(x),orders))

    for idx in range(len(course)):
        if all(list(map(lambda x:x<course[idx],len_order))):
            break

        total_order = sorted(list(set("".join(orders))))
        order_list = [list(orders[i]) for i in range(len(orders))]
        course_example = list(combinations(total_order,course[idx]))
        course_example_dict = collections.defaultdict(list)

        for ce in course_example:
            course_example_dict[ce] = 0

        for order in order_list:

            for ce in course_example:
                for i in range(len(ce)):
                    if not ce[i] in order:
                        break
                else:
                    course_example_dict[ce] += 1

        max_order = max(course_example_dict.values())
        for ce in course_example:
            if(course_example_dict[ce] == max_order and max_order >= 2):
                answer.append("".join(ce))
    answer = sorted(answer)
    return answer

print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"],[2,3,4]))
print(solution(["ABCDE", "AB", "CD", "ADE", "XYZ", "XYZ", "ACD"],[2,3,5]))

