import collections


def solution(record):
    answer = []
    uid_nick = collections.defaultdict(str)
    cur_chat = []
    rec_chat = []
    for r in record:
        r_l = r.split()
        # print(r_l)
        state = r_l[0]
        uid = r_l[1]

        if state == "Enter":
            nick = r_l[2]
            uid_nick[uid] = nick
            rec_chat.append("E " + uid + " " + uid_nick[uid])
        if state == "Leave":
            # cur_chat.pop(cur_chat.index(uid))
            rec_chat.append("L " + uid + " " + uid_nick[uid])
        if state == "Change":
            new_nick = r_l[2]
            uid_nick[uid] = new_nick

    for i, rec in enumerate(rec_chat):
        rec_li = rec.split()
        state = rec_li[0]
        uid = rec_li[1]
        if state == "E":
            rec_chat[i] = uid_nick[uid] + "님이 들어왔습니다."
        else:
            rec_chat[i] = uid_nick[uid] + "님이 나갔습니다."

    return rec_chat


r = ["Enter uid1234 Muzi", "Enter uid4567 Prodo", "Leave uid1234", "Enter uid1234 Prodo", "Change uid4567 Ryan"]

print(solution(r))
