from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_list = [letter for letter in s]
        t_list = [letter for letter in t]
        s_counter = Counter(s_list)
        t_counter = Counter(t_list)
        
        return s_counter == t_counter
        