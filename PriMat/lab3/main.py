import lab3.entities.squareMatrix as squareMatrix

if __name__ == "__main__":
    matrix = squareMatrix.SquareMatrix([
        [1, 0, 5, 0, 3],
        [4, 5, 0, 9, 2],
        [1, 0, 0, 2, 0],
        [0, 0, 3, 0, 0],
        [3, 4, 0, 2, 9]
    ])

    scr_matrix = matrix.to_SCRMatrix()

    print(scr_matrix.data)
    print(scr_matrix.ind)
    print(scr_matrix.ind_ptr)

    square_matrix = scr_matrix.to_SquareMatrix()

    for row in square_matrix.arr:
        print(row)
