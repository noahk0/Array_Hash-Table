def productExceptSelf(self, nums: List[int]) -> List[int]:
    product = [1]

    for i in range(1, len(nums)):
        product.append(product[-1] * nums[i - 1])

    mul = nums[-1]

    for i in range(len(nums) - 2, -1, -1):
        product[i] *= mul
        mul *= nums[i]

    return product
