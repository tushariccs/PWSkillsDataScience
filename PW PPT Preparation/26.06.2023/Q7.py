def monolithic(arr:list[int])->bool:
    x,y =[],[]
    x.extend(arr)
    y.extend(arr)
    x.sort()
    y.sort(reverse=True)
    if(x==arr or y==arr):
        return True
    return False
b = [1,3,2,3]
a = monolithic(b)
print(a)
