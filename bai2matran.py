def create_matrix(n, m):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            # You can initialize the elements with any value you want.
            # Here, I'm using 0 as the default value.
            row.append(0)
        matrix.append(row)
    return matrix

# Example: Create a 3x4 matrix
n = 3
m = 4
matrix = create_matrix(n, m)

# Display the matrix
for row in matrix:
    print(row)
