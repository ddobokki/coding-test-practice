class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        ver1 = version1.split('.')
        ver2 = version2.split('.')

        idx = 0
        max_idx = max(len(ver1),len(ver2))

        while idx < max_idx:
            #print(ver1[idx1],ver2[idx2])
            if int(ver1[idx]) < int(ver2[idx]):
                return -1
            elif int(ver1[idx]) > int(ver2[idx]):
                return 1
            else:
                idx += 1

                if idx >= len(ver1):
                    ver1.append("0")
                if idx >= len(ver2):
                    ver2.append("0")
        return 0



print(Solution().compareVersion(version1 = "1.01", version2 = "1.001"))
print(Solution().compareVersion(version1 = "1.0", version2 = "1.0.0"))
print(Solution().compareVersion(version1 = "0.1", version2 = "1.1"))
print(Solution().compareVersion("1.0.1","1"))
print(Solution().compareVersion(version1 = "7.5.2.4", version2 = "7.5.3"))