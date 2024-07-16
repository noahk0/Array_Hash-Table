def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    freq = [[] for _ in range(len(nums) + 1)]

    for i, num in Counter(nums).items():
        freq[num].append(i)

    top = []

    for lst in freq[::-1]:
        top.extend(lst)

        if k == len(top):
            return top
