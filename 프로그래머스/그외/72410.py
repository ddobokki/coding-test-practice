# https://programmers.co.kr/learn/courses/30/lessons/72410

possible_num = [str(i) for i in range(0,10)]
possible_chars = [chr(i) for i in range(ord('a'), ord('z') + 1)]
possible_special_chars = ["-", "_", "."]
possible_list = possible_chars + possible_special_chars + possible_num


def solution(new_id):
    new_id = list(new_id.lower())
    for idx in range(len(new_id)):
        if not new_id[idx] in possible_list:
            new_id[idx] = ""
    new_id = "".join(new_id)

    while new_id.count("..") != 0:
        new_id = new_id.replace("..", ".")

    new_id = list(new_id)
    if (new_id[0] == "."):
        new_id.pop(0)
    if(len(new_id) > 0):
        if (new_id[-1] == "."):
            new_id.pop()

    if (len(new_id) == 0):
        new_id.append("a")
    if (len(new_id) >= 16):
        new_id = new_id[0:15]
        if (new_id[-1] == "."):
            new_id.pop()

    while len(new_id) <= 2:
        new_id = new_id + list(new_id[-1])

    new_id = "".join(new_id)

    return new_id


print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn.p"))


'''
예1	"...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
예2	"z-+.^."	"z--"
예3	"=.="	"aaa"
예4	"123_.def"	"123_.def"
예5	"abcdefghijklmn.p"	"abcdefghijklmn"

'''