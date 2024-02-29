X = [[1,2],
    [4 ,5],
    [7 ,8]]

T = [[0,0,0],
        [0,0,0]] 

for i in range(len(X)):
    for j in range(len(X[0])):
        T[j][i] = X[i][j]

for i in T:
    print(i)

