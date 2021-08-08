# https://programmers.co.kr/learn/courses/30/lessons/12981

import collections


def solution(n, words):
    total_words = len(words)
    words = collections.deque(words)
    before_words = []
    player_words = [[] for _ in range(n)]
    words_idx = 0

    while words:
        cur_word = words.popleft()

        if not before_words:
            before_words.append(cur_word)
            player_words[words_idx % n].append(cur_word)
            words_idx += 1
            continue

        if not (cur_word in before_words) and (before_words[-1][-1] == cur_word[0]):
            before_words.append(cur_word)
            player_words[words_idx % n].append(cur_word)
        else:
            break

        words_idx += 1

    # for a in player_words:
    #     print(a)
    if words_idx == total_words:
        return [0, 0]
    else:
        return [(words_idx % n) + 1, len(player_words[words_idx % n]) + 1]


# solution(5, ["hello", "observe", "effect", "take", "either", "recognize", "encourage", "ensure", "establish", "hang",
#              "gather", "refer", "reference", "estimate", "executive"])

#solution(2, ["hello", "one", "even", "never", "now", "world", "draw"])

print(solution(3,["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))
