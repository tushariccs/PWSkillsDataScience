class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        for j in range(0,len(nums)):
            if(nums[j]==0):
                pass
            elif(nums[j]!=0):
                nums[j],nums[i] = nums[i],nums[j]
                i+=1
