class Solution:
    def removeElement(self, nums, val: int) -> int:
        if len(nums) == 0:
            return 0
        
        left  = 0
        right = len(nums) - 1

        k = 0
        while left != right:
            if nums[left] == val:
                nums[left] = nums[right]
                nums[right] = '_'
                right -= 1
                k += 1
            else:
                left += 1
        
        if nums[left] == val:
            nums[left] = '_'
            k += 1

        k = len(nums) - k
        return k
    

if __name__ == '__main__':
    nums = [3]
    print(nums)
    solution = Solution()
    k = solution.removeElement(nums, 3)
    print(k)
    print(nums)
