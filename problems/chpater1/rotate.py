# rotate a matrix by 90 degrees.
# A matrix rotation involves first transposing and then
# reveresing each row
# it's a NXN square matrix.

def rotate_matrix(matrix):
    # print(f"the input matrix is {matrix}")
    # num rows
    n=len(matrix)
    # print(f" num rows are {n}")

    # transpose

    for i in range(n):
        for j in range(i+1,n):
            # swap
            matrix[i][j], matrix[j][i]=matrix[j][i], matrix[i][j]

    # reverse each row
    # iterate over the each row in the matrix

    for row in matrix:

        i=0
        j=n-1

        while i<=j:
            # print(f"the row[i] is {row[i]} and row[j] is {row[j]}")
            row[i], row[j]=row[j], row[i]

            i+=1
            j-=1

    return matrix

def main():
    test_cases = [
        # 1x1 matrix (edge case)
        (
            [[1]],
            [[1]]
        ),

        # 2x2 matrix
        (
            [[1, 2],
             [3, 4]],
            [[3, 1],
             [4, 2]]
        ),

        # 3x3 matrix
        (
            [[1, 2, 3],
             [4, 5, 6],
             [7, 8, 9]],
            [[7, 4, 1],
             [8, 5, 2],
             [9, 6, 3]]
        ),

        # 4x4 matrix
        (
            [[5, 1, 9, 11],
             [2, 4, 8, 10],
             [13, 3, 6, 7],
             [15, 14, 12, 16]],
            [[15, 13, 2, 5],
             [14, 3, 4, 1],
             [12, 6, 8, 9],
             [16, 7, 10, 11]]
        ),

        # Non-square input (should ideally raise or return unchanged depending on spec)
        (
            [[1, 2, 3],
             [4, 5, 6]],
            None  # expected behavior depends on implementation
        )
    ]

    print("Testing rotate_matrix:")
    for matrix, expected in test_cases:
        try:
            result = rotate_matrix([row[:] for row in matrix])  # copy to avoid mutation
            status = "✓" if result == expected else "✗"
            print(f"{status} Input {matrix} -> Output {result} (expected {expected})")
        except Exception as e:
            if expected is None:
                print(f"✓ Input {matrix} -> correctly raised {e.__class__.__name__}")
            else:
                print(f"✗ Input {matrix} -> raised {e.__class__.__name__}: {e}")


if __name__ == "__main__":
    main()


   
       
        