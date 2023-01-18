class Solution:
    def isIsomorphic(self, s: str, t: str):
        mapping_s = {}
        mapping_t = {}

        if len(s) != len(t):
            return False
        for i in range(len(s)):
            if s[i] in mapping_s:
                if mapping_s[s[i]] != t[i]:
                    return False
            else:
                if t[i] in mapping_t:
                    return False
                mapping_s[s[i]] = t[i]
                mapping_t[t[i]] = s[i]
        return True
