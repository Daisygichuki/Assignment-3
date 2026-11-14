def to_sparse(m):
    rows, cols = len(m), len(m[0])
    sparse = [[rows, cols, 0]]               # header: rows, cols, non-zero count
    for i in range(rows):
        for j in range(cols):
            if m[i][j] != 0:
                sparse.append([i, j, m[i][j]])
    sparse[0][2] = len(sparse) - 1
    return sparse

matrix = [[0, 0, 3, 0, 0],
          [0, 0, 0, 0, 5],
          [0, 7, 0, 0, 0],
          [0, 0, 0, 9, 0]]

print("Row Col Value")
for row in to_sparse(matrix):
    print(*row)
