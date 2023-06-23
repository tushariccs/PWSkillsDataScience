
def Find_element(nums:list[int],target:int)->int:
        low = 0
        high = len(nums)-1
        mid = 0
        while low<=high:
            mid = (low+high)//2
            if nums[mid]>target:
                high = mid - 1
            elif nums[mid]<target:
                low = mid + 1
            else:
                return mid
        return -1
    
arr = [2, 3, 4, 10, 40 ]
x = 10
 
# Function call
result = Find_element(arr, x)
 
if result != -1:
    print("Element is present at index", str(result))
else:
    print("Element is not present in array")