
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen = {}
        for words in strs:
            x = "".join(sorted(words))
            if x not in seen:
                seen[x] = [words]
            else:
                seen[x].append(words)
        return list(seen.values())   
            
        
        