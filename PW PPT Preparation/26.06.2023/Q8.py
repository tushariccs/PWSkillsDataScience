def addition_with_value(nums:list[int],x:int)->int:
    n = []
    i = 0
    while i<len(nums):
        n.append(nums[i]+x)
        i+=1
    return (max(n) - min(n))

a = [1,2,3,4,5,6]
k = 3
c = addition_with_value(a,k)
print(c)
