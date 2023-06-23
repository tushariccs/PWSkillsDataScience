# def sum_upto_target(arr:list,target:int)->int:
#     #If the array is empty
#     if len(arr)==0:
#         return 0
    
#     sum = arr[0]
#     for i in range (0,len(arr)):
#         sum = arr[i] + arr[i+1]
#         if sum == target:
#             return i,i+1
  
# a = [2,7,11,15]
# target = 17
# b =  sum_upto_target(a,target)
# print(f"[{b}]")


# def twoSums(nums,target):
#     num2={}
#     for i,num in enumerate(nums):
#         match = target - num
#         if match in num2:
#             return [num2[match,i]]
#         num2[num]=i
        
        
# a = [2,7,11,15]
# target = 26
# a = twoSums(a,target)
# print(a)

        