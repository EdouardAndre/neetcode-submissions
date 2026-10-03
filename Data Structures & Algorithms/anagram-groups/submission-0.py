class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            histo = 26 * [0]
            for i in word:
                histo[ord(i) - ord('a')] += 1
            d[tuple(histo)].append(word)
        return list(d.values())