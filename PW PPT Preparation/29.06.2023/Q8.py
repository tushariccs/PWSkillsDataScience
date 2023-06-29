class Solution:
 def shuffle(self, nums: list[int], n: int) -> list[int]:
        ls=[]
        for i in range(n):
            ls+=[nums[i]]
            ls+=[nums[i+n]]
        return ls