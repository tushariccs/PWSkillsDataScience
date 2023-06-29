def ArrayPartition(arr:list[int]):
    arr.sort()
    sum = 0
    for i in range (0,len(arr),2):
        sum+=arr[i]
    return sum

a = ArrayPartition([1,4,3,2])
print(a)