"""
Group Anagrams:
Given an array of strings, group anagrams together.

"""
from collections import defaultdict
class Solution:
    """
    :type strs: List[str]
    :rtype: List[List[str]]
    """
    def groupAnagrams(self, strs):
        ans  = defaultdict(list)
        
        for s in strs:
            ans[tuple(sorted(s))].append(s)
        return ans.values()
