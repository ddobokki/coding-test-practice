# https://programmers.co.kr/learn/courses/30/lessons/72412
import collections

def solution(info, query):
    answer = []

    lang = collections.defaultdict(list)
    job_group = collections.defaultdict(list)
    career = collections.defaultdict(list)
    food = collections.defaultdict(list)
    score = collections.defaultdict()
    info = list(map(lambda x: x.split(), info))

    for person, i in enumerate(info):
        lang[i[0]].append(person)
        job_group[i[1]].append(person)
        career[i[2]].append(person)
        food[i[3]].append(person)
        score[person] = int(i[4])
    lang["-"] = list(range(len(info)))
    job_group["-"] = list(range(len(info)))
    career["-"] = list(range(len(info)))
    score["-"] = list(range(len(info)))
    food["-"] = list(range(len(info)))

    query = list(map(lambda x: x.replace("and", " ").split(), query))
    # print(query)

    for q in query:
        lang_condi = q[0]
        job_condi = q[1]
        career_condi = q[2]
        food_condi = q[3]
        score_condi = int(q[4])

        lang_set = set(lang[lang_condi])
        job_set = set(job_group[job_condi])
        career_set = set(career[career_condi])
        food_set = set(food[food_condi])
        if len(lang_set) == 0 or len(job_set) ==0 or len(career_set) ==0 or len(food_set) == 0:
            answer.append(0)
            continue
        all_clear_person = list(lang_set.intersection(job_set).intersection(career_set).intersection(food_set))

        cnt = 0
        for acp in all_clear_person:
            if score[acp] >= score_condi:
                cnt += 1
        answer.append(cnt)
    # print(answer)
    return answer

'''
로직은 통과, 효율성은 비통과
'''


infos = ["java backend junior pizza 150", "python frontend senior chicken 210",
         "python frontend senior chicken 150", "cpp backend senior pizza 260",
         "java backend junior chicken 80", "python backend senior chicken 50"]

querys = ["java and backend and junior and pizza 100",
          "python and frontend and senior and chicken 200",
          "cpp and - and senior and pizza 250",
          "- and backend and senior and - 150",
          "- and - and - and chicken 100",
          "- and - and - and - 150"]
solution(infos, querys)
