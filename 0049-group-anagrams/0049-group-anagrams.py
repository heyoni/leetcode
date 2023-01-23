class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict_strs = {}
        for i in strs:
            dict_strs[''.join(sorted(i))] = []

        for j in strs:
            dict_strs[''.join(sorted(j))].append(j)

        return [*dict_strs.values()]