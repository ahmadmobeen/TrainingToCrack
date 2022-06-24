class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        
        rev1 = version1.split('.')
        rev2 = version2.split('.')

        
        n1, n2 = len(rev1), len(rev2)
        n = max(n1, n2)
        
        for i in range(n):
            i1 = int(rev1[i]) if i < n1 else 0
            i2 = int(rev2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1
        return 0
