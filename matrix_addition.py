def main():
    print("This program adds two matrices.")
    # take the row and column number from user
    row = int(input("Enter the number of rows: "))
    column = int(input("Enter the number of columns: "))
    if row != column:
        print("The matrices cannot be added. ")
    else:
        # initialize matrix
        matrix1 = []
        # take the user entry for first element
        print("Enter the entries row-wise: ")
        for i in range(row):
            a = []
            for j in range(column):
                a.append(int(input()))
            matrix1.append(a)

        matrix2 = []
        # take the user entry for second matrix
        print("Enter the entries row wise: ")
        for i in range(row):
            b = []
            for j in range(column):
                b.append(int(input()))
            matrix2.append(b)
        # initialize a result matrix
        result = []
        for i in range(row):
            c = []
            for j in range(column):
                c.append(matrix1[i][j] + matrix2[i][j])
            result.append(c)
        print("The addition of matrix is", result)


if __name__ == '__main__':
    main()
