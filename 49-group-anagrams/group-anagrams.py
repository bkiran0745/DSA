class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        keep = {}
        for i in strs:
            s = "".join(sorted(i))
            if s in keep:
                keep[s].append(i)
            else:
                keep[s] = [i]
        re = []
        for i,k in keep.items():
            re.append(k)
        return re
        