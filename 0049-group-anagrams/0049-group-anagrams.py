class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for s in strs:
            sorted_word = "".join(sorted(s))
            groups[sorted_word].append(s)


        return list(groups.values())
