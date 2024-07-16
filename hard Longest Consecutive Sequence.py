def longestConsecutive(self, nums: List[int]) -> int:
    longest = 0
    nums = set(nums)

    for num in nums:
        if (num - 1) not in nums:
            consec = num + 1

            while consec in nums:
                consec += 1

            longest = max(longest, consec - num)

    return longest
