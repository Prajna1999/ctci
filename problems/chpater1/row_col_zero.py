# if any element in the row or column is zero.
# Make the entire row/column zero
# needn't know which element is zero, instead
# only need to store the info about having atleast one zero element 
# in a row or column

def row_col_zero(matrix):
    # size of the matrix MXN
    # row count
    m=len(matrix)

    #column count
    n=len(matrix[0])

    row_zeros=[False]*m
    col_zeros=[False]*n

    # loop through the matrix and toggle for rows
    # and cols containing atleast one zero element
    for i in range(m):
        for j in range(n):
            if matrix[i][j]==0:
                row_zeros[i]=True
                col_zeros[j]=True

    
    # loop through the row_zeros list and nullify the rows
    for i in range(m):
        if row_zeros[i]:
            # nullify that row by zeroing all columns for that row
            for j in range(n):
                matrix[i][j]=0
    
    # loop through the col_zeros list and nullify the columns
    for j in range(n):
        if col_zeros[j]:
            for i in range(m):
                matrix[i][j]=0
    
    return matrix

def main():
    test_cases = [
        # No zeros (should remain unchanged)
        (
            [[1, 2], 
             [3, 4]],
            [[1, 2],
             [3, 4]]
        ),

        # Single zero in middle
        (
            [[1, 2, 3],
             [4, 0, 6],
             [7, 8, 9]],
            [[1, 0, 3],
             [0, 0, 0],
             [7, 0, 9]]
        ),

        # Zeros in first row and last column
        (
            [[0, 2, 3],
             [4, 5, 6],
             [7, 8, 0]],
            [[0, 0, 0],
             [0, 5, 0],
             [0, 0, 0]]
        ),

        # Entire matrix already zeros
        (
            [[0, 0],
             [0, 0]],
            [[0, 0],
             [0, 0]]
        ),

        # Single row with zero
        (
            [[1, 0, 3, 4]],
            [[0, 0, 0, 0]]
        ),

        # Single column with zero
        (
            [[1],
             [0],
             [3]],
            [[0],
             [0],
             [0]]
        ),

        # Larger case: multiple zeros
        (
            [[5, 1, 9, 0],
             [2, 0, 8, 10],
             [13, 3, 6, 7],
             [15, 14, 12, 16]],
            [[0, 0, 0, 0],
             [0, 0, 0, 0],
             [13, 0, 6, 0],
             [15, 0, 12, 0]]
        ),
    ]

    print("Testing row_col_zero:")
    for matrix, expected in test_cases:
        original = [row[:] for row in matrix]  # preserve input
        result = row_col_zero([row[:] for row in matrix])
        status = "✓" if result == expected else "✗"
        print(f"{status} Input {original} -> Output {result} (expected {expected})")


if __name__ == "__main__":
    main()

