
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        seen = {}
        for s in strs:
            letters = list(s)
            letters.sort()
            label = "".join(letters)
            if label not in seen:
                seen[label] = [s]
            else:
                seen[label].append(s)
            
        return [grp for grp in seen.values()]    
            
        
        