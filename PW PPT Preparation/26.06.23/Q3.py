# def index_of_sort(arr:list,target:int)->int:
#     # arr = arr.sort()
    
#     for i in range(0,len(arr)):
#         if arr[i] == target:
#             return i
#         elif arr[i]<target:
#             return i+1
#         else: 
#           return i-1
       
def searchInsert(nums, target):
    left_side = 0
    right_side = len(nums) - 1

    while left_side <= right_side:
        mid = int((left_side + right_side) / 2)

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left_side = mid + 1
        else:
            right_side = mid - 1

    return left_side
       
nums = [1,3,5,6]
target = 4
a = searchInsert(nums,target)   
print(a)