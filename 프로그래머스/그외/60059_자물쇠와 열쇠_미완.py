# https://programmers.co.kr/learn/courses/30/lessons/60059

def input_key(key, lock):
    return list(map(lambda x, y: x ^ y, key, lock))


def rotation(key):
    # 배열을 시계 방향으로 회전시키는 함수
    rotation_key = [[0] * len(key[0]) for _ in range(len(key))]
    N = len(key)
    for x in range(N):
        for y in range(N):
            rotation_key[y][x] = key[N - x - 1][y]

    return rotation_key


def solution(key, lock):
    # 아이디어 : 키를 움직이면서 lock과 or 연산을 한다.
    # 없으면 90도 회전해서 처음부터
    # 3번 회전시켜도 없으면 false를 리턴

    # 완전히 겹쳐지게 먼저 연산
    # key와 lock을 1차원으로 만들어준다

    lock_1d = []
    for l in lock:
        lock_1d += l

    M = len(lock_1d)
    for _ in range(4):
        key = rotation(key)
        key_1d = []

        for k in key:
            key_1d += k
        N = len(key_1d)
        for i in range(N - 1):
            lock_1d_c = lock_1d.copy()
            temp = input_key(key_1d[-i - 1:], lock_1d_c[:i + 1])
            lock_1d_c[:i + 1] = temp
            #print(lock_1d_c)
            if all(lock_1d_c):
                return True
        for i in range(M - N):
            lock_1d_c = lock_1d.copy()
            temp = input_key(key_1d, lock_1d[i:i + N])
            lock_1d_c[i:i + N] = temp
            #print(lock_1d_c)
            if all(lock_1d_c):
                return True
        for i in range(N - 1):
            lock_1d_c = lock_1d.copy()
            temp = input_key(key_1d[:-i - 1], lock_1d_c[M - N + 1 + i:])
            lock_1d_c[M - N + 1 + i:] = temp
            #print(lock_1d_c)
            if all(lock_1d_c):
                return True

    return False


keys = [[0, 0, 0], [1, 0, 0], [0, 1, 1]]
locks = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
print(solution(keys,locks))
# r = rotation(keys)
# # for rr in r:
# #     print(rr)
# # a = [[1,1],[0,0]]
# # b = [[0,0],[1,1]]
# # c = input_key(a,b)
# # print(c)
# print(r)
# locks = [[1, 1, 1],
#          [1, 1, 0],
#          [1, 0, 1]]
# solution(r, locks)
# c = [1, 2, 3]
# #print(c[:1])
#
# print(0^1)