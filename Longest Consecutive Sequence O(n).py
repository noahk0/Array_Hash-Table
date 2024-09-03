def longestConsecutive(self, nums: List[int]) -> int:
    longest, nums = 0, set(nums)

    for num in nums:
        if (num - 1) in nums:
            continue
            
        consec = num + 1

        while consec in nums:
            consec += 1

        longest = max(longest, consec - num)

    return longest
