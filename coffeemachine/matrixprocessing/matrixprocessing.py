def get_matrix():
    try:
        size_input = input("Enter matrix size: ").split()
        rows_n, cols_m = int(size_input[0]), int(size_input[1])
        print("Enter matrix:")
        matrix_data = []
        for _ in range(rows_n):
            row_data = [float(x) for x in input().split()]
            matrix_data.append(row_data)
        return matrix_data, rows_n, cols_m
    except (ValueError, IndexError):
        return None, 0, 0


def print_matrix(matrix_to_print):
    print("The result is:")
    for row in matrix_to_print:
        print(*(f"{x:g}" for x in row))


def add_matrices():
    m1, r1, c1 = get_matrix()
    m2, r2, c2 = get_matrix()
    if m1 and m2 and r1 == r2 and c1 == c2:
        res = [[m1[i][j] + m2[i][j] for j in range(c1)] for i in range(r1)]
        print_matrix(res)
    else:
        print("The operation cannot be performed.")


def multiply_by_const():
    m_data, r_n, c_m = get_matrix()
    if m_data:
        const_val = float(input("Enter constant: "))
        res = [[m_data[i][j] * const_val for j in range(c_m)] for i in range(r_n)]
        print_matrix(res)


def multiply_matrices():
    m1, r1, c1 = get_matrix()
    m2, r2, c2 = get_matrix()
    if m1 and m2 and c1 == r2:
        res = [[sum(m1[i][k] * m2[k][j] for k in range(c1)) for j in range(c2)] for i in range(r1)]
        print_matrix(res)
    else:
        print("The operation cannot be performed.")


def transpose_matrix():
    print("\n1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
    trans_choice = input("Your choice: ")
    m_data, r_n, c_m = get_matrix()
    if not m_data:
        return

    res = []
    if trans_choice == '1':
        res = [[m_data[j][i] for j in range(r_n)] for i in range(c_m)]
    elif trans_choice == '2':
        res = [[m_data[r_n - 1 - j][c_m - 1 - i] for j in range(r_n)] for i in range(c_m)]
    elif trans_choice == '3':
        res = [row[::-1] for row in m_data]
    elif trans_choice == '4':
        res = m_data[::-1]

    if res:
        print_matrix(res)


def get_determinant(m_input):
    if len(m_input) == 1:
        return m_input[0][0]
    if len(m_input) == 2:
        return m_input[0][0] * m_input[1][1] - m_input[0][1] * m_input[1][0]
    det_val = 0
    for j in range(len(m_input)):
        minor = [row[:j] + row[j + 1:] for row in m_input[1:]]
        det_val += ((-1) ** j) * m_input[0][j] * get_determinant(minor)
    return det_val


def inverse_matrix():
    m_data, r_n, c_m = get_matrix()
    if r_n != c_m or not m_data:
        print("This matrix doesn't have an inverse.")
        return
    det_val = get_determinant(m_data)
    if det_val == 0:
        print("This matrix doesn't have an inverse.")
        return

    adjugate = []
    for i in range(r_n):
        adj_row = []
        for j in range(c_m):
            minor = [row[:j] + row[j + 1:] for row in (m_data[:i] + m_data[i + 1:])]
            adj_row.append(((-1) ** (i + j)) * get_determinant(minor))
        adj_row_data = adj_row
        adjugate.append(adj_row_data)

    trans_adj = [[adjugate[j][i] for j in range(r_n)] for i in range(c_m)]
    res_inverse = [[val / det_val for val in row] for row in trans_adj]
    print_matrix(res_inverse)


def main_menu():
    while True:
        print("\n1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices")
        print("4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
        user_choice = input("Your choice: ")
        if user_choice == '1':
            add_matrices()
        elif user_choice == '2':
            multiply_by_const()
        elif user_choice == '3':
            multiply_matrices()
        elif user_choice == '4':
            transpose_matrix()
        elif user_choice == '5':
            m_data, r_n, c_m = get_matrix()
            if m_data:
                print(f"The result is:\n{get_determinant(m_data):g}")
        elif user_choice == '6':
            inverse_matrix()
        elif user_choice == '0':
            break


if __name__ == "__main__":
    main_menu()