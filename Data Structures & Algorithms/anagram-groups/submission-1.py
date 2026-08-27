class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tracker = defaultdict(list)
        for s in strs:
            cur_table = [0] * 26
            for char in s:
                cur_table[ord(char) - ord('a')] += 1
            tracker[tuple(cur_table)].append(s)
        return list(tracker.values())


        