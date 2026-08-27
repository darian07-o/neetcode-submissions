class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        table = [0] * 26
        for char in s:
            table[ord(char) - ord('a')] += 1
        table2 = [0] * 26
        for char in t:
            table2[ord(char) - ord('a')] += 1;
        return table == table2

        
        