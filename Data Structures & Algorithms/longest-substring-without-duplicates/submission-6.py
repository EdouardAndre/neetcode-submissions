class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr_win = set()
        res = 0
        curr = 0
        i = 0
        j = 0
        while i < len(s):
            if s[i] in curr_win:
                res = max(res, curr)
                while j < i and s[i] in curr_win:
                    curr_win.remove(s[j])
                    j += 1
                    curr -= 1 
                curr += 1
                curr_win.add(s[i])
            else:
                curr += 1
                curr_win.add(s[i])
            i += 1
            
        return max(res, curr)