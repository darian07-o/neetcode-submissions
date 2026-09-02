class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        mp = {}
        res = 0
        maxF = 0

        l = 0
        for r in range(len(s)):
            mp[s[r]] = 1 + mp.get(s[r], 0)
            maxF = max(maxF, mp[s[r]])

            if (r - l + 1) - maxF > k:
                mp[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        return res


        