
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        # seen = {}
        # for words in strs:
        #     x = "".join(sorted(words))
        #     if x not in seen:
        #         seen[x] = [words]
        #     else:
        #         seen[x].append(words)
        # return list(seen.values())   
    
        
        seen = {}
        for word in strs:
            joined = "".join(sorted(word))
            if joined not in seen:
                seen[joined] = [word]
            else:
                seen[joined].append(word)
        return list(seen.values())
        