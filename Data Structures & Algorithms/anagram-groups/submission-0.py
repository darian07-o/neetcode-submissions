class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        checker = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for letter in s:
                count[ord(letter) - ord('a')] += 1;
            checker[tuple(count)].append(s)
        return list(checker.values())
        