class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        count = 0
        while left != right:
            left >>= 1
            right >>= 1
            count += 1

        # 같은 구간까지 비트를 오른쪽으로 옮김
        # 만약 끝까지 다르게 되면 0이 되버림(32번 시프트해서)
        # 101, 100 이라면 한번만 시프트 하면 되기 때문에 10에서 100으로 카운트 만큼 쉬프트해준게 답
        return left << count

#
# print("{0:032b}".format(600000000))
#
#
# print("{0:032b}".format(2147483645))
print(Solution().rangeBitwiseAnd(6,7))