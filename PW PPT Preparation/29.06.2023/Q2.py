def Intersection(arr1:list[int],arr2:list[int])->list[int]:
    arr = set(arr1)
    arr3 = set(arr2)
    r1 = list(set(x for x in arr1 if x not in arr3))
    r2 = list(set(y for y in arr2 if y not in arr))
    return [r1,r2]
a = Intersection(arr1=[1,2,3],arr2=[2,4,6])
print(a)