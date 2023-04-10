class Solution:
    def removeDuplicates(self, nums) -> int:
        if len(nums) == 1:
            return 1, nums
        
        unrepeat_num = None
        unrepeat_index = 0
        k = 0
        for index, num in enumerate(nums):
            if unrepeat_num != num and unrepeat_num is None:
                unrepeat_num = num
                unrepeat_index = index
                k += 1
            elif unrepeat_num != num:
                unrepeat_num = num
                nums[index], nums[unrepeat_index + 1] = nums[unrepeat_index + 1], num
                unrepeat_index += 1
                k += 1

        return k, nums
    

s = Solution()

print(s.removeDuplicates([1,1,2]))
print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
        