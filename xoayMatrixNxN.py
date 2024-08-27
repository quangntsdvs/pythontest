def create_matrix(n):
    matrix = [[i + j * n + 1 for i in range(n)] for j in range(n)]
    return matrix

def rotate_matrix(matrix):
    n = len(matrix)

    for layer in range(n // 2):
        first = layer
        last = n - 1 - layer

        for i in range(first, last):
            offset = i - first
            top = matrix[first][i]
            matrix[first][i] = matrix[last - offset][first]
            matrix[last - offset][first] = matrix[last][last - offset]
            matrix[last][last - offset] = matrix[i][last]
            matrix[i][last] = top

# Ví dụ
n = 3
ma_tran_goc = create_matrix(n)

print("Ma Trận Gốc:")
for hang in ma_tran_goc:
    print(hang)
rotate_matrix(ma_tran_goc)
print("\nMa Trận Sau Khi Xoay 90 Độ:")
for hang in ma_tran_goc:
    print(hang)
