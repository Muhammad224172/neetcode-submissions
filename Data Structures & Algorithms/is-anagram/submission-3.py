class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        checked = []

        if len(s) != len(t): 
            return False 
    
        else: 
            return sorted(s) == sorted(t)
        