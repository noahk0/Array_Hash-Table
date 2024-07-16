def twoSum(self, nums: List[int], target: int) -> List[int]:
    pre = {}

    for i in range(len(nums)):
        if target - nums[i] in pre:
            return (pre[target - nums[i]], i)

        pre[nums[i]] = i
