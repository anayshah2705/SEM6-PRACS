print("Enter the size of matrix X (rows columns):")
X_rows, X_cols = map(int, input().split())
print("Enter the size of matrix Y (rows columns):")
Y_rows, Y_cols = map(int, input().split())
print("Enter elements of matrix X:")
X = []
for i in range(X_rows):
    row = list(map(int, input().split()))
    X.append(row)
print("Enter elements of matrix Y:")
Y = []
for i in range(Y_rows):
    row = list(map(int, input().split()))
    Y.append(row)
result = [[0 for _ in range(Y_cols)] for _ in range(X_rows)]

def mapper(i, j):
    partial_result = 0
    for k in range(len(Y)):
        partial_result += X[i][k] * Y[k][j]
    return (i, j, partial_result)

def reducer(results):
    for i, j, partial_result in results:
        result[i][j] = partial_result

mapped_values = [mapper(i, j) for i in range(X_rows) for j in range(Y_cols)]
reducer(mapped_values)
print("Result of matrix multiplication:")
for r in result:
    print(r)