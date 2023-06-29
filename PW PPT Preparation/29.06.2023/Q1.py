def Insertection_of_array(arr1:list[int],arr2:list[int],arr3:list[int])->list[int]:
    arr1.sort()
    arr2.sort()
    arr3.sort()
   
    def find(arr,val):
        for i in arr:
            if i == val:
                return val
    res = []
    for num in arr1:
        if find(arr2,num) and find(arr3,num):
            res.append(num)
    return res

arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]
a = Insertection_of_array(arr1,arr2,arr3)
print(a)