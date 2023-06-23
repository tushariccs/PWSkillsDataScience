
from collections import Counter
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        c = Counter(nums)
        # print(type(c))
        l=[0,0]
        for i in range(1,len(nums)+1):
            if c[i]==2:
                l[0]=i
            if c[i]==0:
                l[1]=i
        return l
#c stores {2:2,1:1,4:1}
'''
l = [0,0]
c[1]==2
l[0] = 2
'''
a = Solution()
nums = [1,2,2,4]
c = a.findErrorNums(nums)
print(c)