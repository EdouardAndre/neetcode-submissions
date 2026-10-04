class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        d = defaultdict(int)
        max_curr = 0
        res = 0
        i = 0
        j = 0
        while j < len(s):
            d[s[j]] += 1
            if d[s[j]] > max_curr:
                max_curr = d[s[j]]
            if (j - i + 1) - max_curr > k:
                d[s[i]] -= 1
                i += 1
            else:
                res = max(res, j-i + 1)
            j += 1
        return res
                
                
            
            
        