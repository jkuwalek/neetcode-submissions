from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        s_list = []
        t_list = []

        for letter in s:
            s_list.append(letter)
        
        for letter in t:
            t_list.append(letter)

        s_counter = Counter(s_list)
        t_counter = Counter(t_list)
        
        
        return s_counter == t_counter
        # list_s = s.strip()
        # counter_s, counter_d = Counter(s), Counter(d)
        # return counter_s == counter_d
        