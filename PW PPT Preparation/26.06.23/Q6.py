class Solution:
        def containsDuplicate(self, nums: list[int]) -> bool:  
            hash_Set = set()
            for i in nums:
                if i in hash_Set:
                    return True
                else:
                    hash_Set.add(i)