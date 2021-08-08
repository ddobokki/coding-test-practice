def solution(msg):
    answer = []

    word_dict = {}
    idx = 1
    for i in range(ord('A'), ord('Z') + 1):
        word_dict[chr(i)] = idx
        idx += 1

    cur_word = ''
    i = 0
    n_i = 0
    while i < len(msg):

        for j in range(0, len(msg)):

            if not msg[i: i + j+1] in word_dict:
                word_dict[msg[i: i + j+1]] = idx
                idx += 1

                break
            else:
                cur_word = msg[i: i + j+1]
                n_i = j+1
        i += n_i
        #print(i)
        if cur_word != '':
            answer.append(word_dict[cur_word])
    return answer

solution('A')
s= "abc"
print(s[2:4])