import collections


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        sortMap = collections.defaultdict(list)
        for word in strs:
            sortMap[tuple(sorted(word))].append(word)
    
        return sortMap.values()
        
    