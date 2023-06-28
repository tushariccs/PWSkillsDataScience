import itertools
nums = [1,2,3]
a = list(itertools.permutations(nums,len(nums)))
print(a)