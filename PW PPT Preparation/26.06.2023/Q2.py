def Alice_candies(candies:list[int])->int:
    a = set(candies)
    a = sum(a)
    print(a/2)
    
a = [1,1,2,2,3,3]
Alice_candies(a)