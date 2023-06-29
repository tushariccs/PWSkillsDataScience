def Transpose(arr1:list[list[int]]):
    rows = len(arr1)
    cols = len(arr1[0])
    arr = [[0 for _ in range(rows)]for _ in range(cols)]
    for i in range(0,rows):
        for j in range (0,cols):
            arr[j][i] = arr1[i][j] 
    return arr

a = Transpose([[1,2,3],[4,5,6],[7,8,9]])
print(a)