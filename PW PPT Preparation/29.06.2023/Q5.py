def staircase(n:int)->int:
    i = 1
    res = 0
    while(n>=i):
        n-=i
        res+=1
        i+=1
    return res
        
a = staircase(8)
print(a)