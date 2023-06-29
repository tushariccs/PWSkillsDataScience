def sqaure_sort(num:list[int])->list[int]:
    res = []
    for i in num:
        a = i*i
        res.append(a)
    res.sort()
    return res

a = sqaure_sort(num = [-4,-1,0,3,10])
print(a)

# num = [-4,-1,0,3,10]
# num.sort()
# print(num)