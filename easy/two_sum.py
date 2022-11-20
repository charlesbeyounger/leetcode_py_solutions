class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        result = []
        for index1, num1 in enumerate(nums):
            for index2, num2 in enumerate(nums[index1 + 1:]):
                if num1 + num2 == target:
                    return [index1, index1 + index2 + 1]