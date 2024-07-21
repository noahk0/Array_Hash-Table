def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    group = defaultdict(list)

    for s in strs:
        count = [0] * 26

        for char in s:
            count[ord(char) - ord('a')] += 1

        group[tuple(count)].append(s)

    return group.values()
