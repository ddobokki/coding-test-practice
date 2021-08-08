def get_head_num(s):
    idx = 0

    file_name = ''
    while not s[idx].isdigit():
        file_name += s[idx]
        idx += 1

    file_num = ''
    while idx < len(s):
        if s[idx].isdigit():
            file_num += s[idx]
        else:
            break
        idx += 1

    file_tail = s[idx:]

    return [file_name,file_num,file_tail]

def solution(files):
    answer = []


    for file in files:
        answer.append(get_head_num(file))

    answer.sort(key=lambda x:(x[0].lower(),int(x[1])))
    answer = list(map(lambda x:''.join(x),answer))
    return answer


solution( ["img12.png", "img10.png", "img02.png", "img1.png", "IMG01.GIF", "img2.JPG"])
solution( ["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"])