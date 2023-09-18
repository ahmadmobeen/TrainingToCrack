class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        n_s = len(s)
        n_t = len(t)
        j = 0
        i = 0
        if n_s == 0:
            return True
        while j < n_t:
            if s[i] == t[j]:
                i += 1
            j += 1
            if i == n_s:
                return True
        return False

