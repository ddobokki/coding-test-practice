class Solution:
    def is_sub_add(self,s1,s2,s3):
        return int(s1) + int(s2) == int(s3)

    def isAdditiveNumber(self, num: str) -> bool:
        if len(num) < 3:
            return False

        left = 0
        p1 = 1
        p2 = 2
        fin = 3
        check_num = num[left:fin]
        print(check_num)
        print(check_num[:p1],check_num[p1:p2],check_num[p2:fin])
        pass

        # while fin < len(num):
        #     check_num = num[left:fin]
        #     if self.is_sub_add(check_num[:p1],check_num[p1:p2],check_num[p2:fin]):

        return True
Solution().isAdditiveNumber("112358")
# Solution().isAdditiveNumber("112358")
# Solution().isAdditiveNumber("112358")