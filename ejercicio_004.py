x = ((1, 2, 3),
     (4, 5, 6))
y = ((-1, 0),
     (0, 1),
     (1,1))

result = [[0,0],
          [0,0]]
for i in range(len(x)):
    for j in range(len(y[0])):
        for k in range(len(y)):
            result[i][j] += x[i][k] * y[k][j]
for i in range(len(result)):
    result[i] = tuple(result[i])
result = tuple(result)
for i in range(len(result)):
    print(result[i])