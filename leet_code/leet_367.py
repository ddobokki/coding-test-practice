class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        return num**0.5 == int(num**0.5)


'''
sqrt를 사용하지 않을경우
class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1:
            return True
        def perfectSquare(num, l=0, r=num):
            if l > r:
                return False
            m = (l + r) // 2
            m_2 = m**2
            if m_2 == num:
                return True
            if m_2 > num:
                return perfectSquare(num, l, m-1)
            if m_2 < num:
                return perfectSquare(num, m+1, r)
        return perfectSquare(num)

'''