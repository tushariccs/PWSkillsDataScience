def Q4(arr:list)->str:
    ans = 0
 
    for i in range(0,3):
        if i==0:
            ans = ans + arr[i]*100
        elif i==1:
            ans = ans + arr[i]*10
        elif i==2:
            ans = ans + arr[i]*1
    return str(ans+1)

a = Q4([1,2,3])
print(list(a))
# a = [1,2,3]
# print(a.index(3))