class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:

        for j in range (n):
            nums1[m+j] = nums2[j]
        nums1.sort()

b = Solution()
nums1 = [1,2,3]
m = 3 
nums2 = [2,5,6] 
n = 3
a = b.merge(nums1,nums2,m,n)
print(a)