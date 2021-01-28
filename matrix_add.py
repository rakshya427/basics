def main():
    A = [[1, 2, 3],
        [4, 5, 6]]
    B = [[1, 2, 3],
        [4, 5, 6]]
    result = [[0, 0, 0],
              [0, 0, 0]]
    # traverse through rows
    for i in range(len(A)):
        # traverse through columns
        for j in range(len(A[0])):
            result[i][j] = A[i][j] + B[i][j]
        for r in result:
            print(r)


if __name__ == '__main__':
    main()