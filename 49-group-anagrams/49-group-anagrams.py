class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for x in strs:
            srt = "".join(sorted(x))
            if srt in groups:
                groups[srt] += [x]
            else:
                groups[srt] = [x]
        print(groups.values())
        return groups.values()