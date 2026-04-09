class Matrix:
    def __init__(self, data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0]) if self.rows > 0 else 0

    def print_matrix(self):
        for row in self.data:
            print(' '.join(map(lambda x: str(int(x) if x == int(x) else round(x, 2)), row)))

    def add(self, other):
        if self.rows != other.rows or self.cols != other.cols:
            print("ERROR")
            return None
        result = [[self.data[i][j] + other.data[i][j] for j in range(self.cols)]
                  for i in range(self.rows)]
        return Matrix(result)

    def multiply_constant(self, c):
        result = [[elem * c for elem in row] for row in self.data]
        return Matrix(result)

    def multiply_matrix(self, other):
        if self.cols != other.rows:
            print("The operation cannot be performed.")
            return None
        result = [[sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                   for j in range(other.cols)] for i in range(self.rows)]
        return Matrix(result)

    def transpose(self, mode=1):
        if mode == 1:
            result = [[self.data[j][i] for j in range(self.rows)] for i in range(self.cols)]
        elif mode == 2:
            result = [[self.data[self.rows - 1 - j][self.cols - 1 - i] for j in range(self.rows)]
                      for i in range(self.cols)]
        elif mode == 3:
            result = [list(reversed(row)) for row in self.data]
        elif mode == 4:
            result = list(reversed(self.data))
        else:
            return None
        return Matrix(result)

    def determinant(self):
        if self.rows != self.cols:
            return None
        return self._det_recursive(self.data)

    def _det_recursive(self, matrix):
        n = len(matrix)
        if n == 1: return matrix[0][0]
        if n == 2: return matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
        det = 0
        for c in range(n):
            minor = [row[:c] + row[c + 1:] for row in matrix[1:]]
            det += ((-1) ** c) * matrix[0][c] * self._det_recursive(minor)
        return det

    def inverse(self):
        det = self.determinant()
        if det == 0 or det is None:
            print("This matrix doesn't have an inverse.")
            return None
        n = self.rows
        cofactors = []
        for r in range(n):
            cofactor_row = []
            for c in range(n):
                minor = [row[:c] + row[c + 1:] for i, row in enumerate(self.data) if i != r]
                cofactor_row.append(((-1) ** (r + c)) * self._det_recursive(minor))
            cofactors.append(cofactor_row)

        adjugate = [[cofactors[j][i] for j in range(n)] for i in range(n)]
        inv = [[adjugate[i][j] / det for j in range(n)] for i in range(n)]
        return Matrix(inv)


def read_matrix(label=""):
    try:
        size = input(f"Enter size of {label}matrix: > ").split()
        n, m = int(size[0]), int(size[1])
        data = []
        print(f"Enter {label}matrix:")
        for _ in range(n):
            data.append(list(map(float, input("> ").split())))
        return Matrix(data)
    except:
        return None


def main():
    while True:
        print("\n1. Add matrices\n2. Multiply matrix by a constant\n3. Multiply matrices")
        print("4. Transpose matrix\n5. Calculate a determinant\n6. Inverse matrix\n0. Exit")
        choice = input("Your choice: > ")

        if choice == '1':
            A = read_matrix("first ")
            B = read_matrix("second ")
            res = A.add(B) if A and B else None
            if res: res.print_matrix()

        elif choice == '2':
            A = read_matrix()
            if A:
                try:
                    c = float(input("Enter constant: > "))
                    A.multiply_constant(c).print_matrix()
                except ValueError:
                    print("Error: Invalid input. Constant must be a number.")

        elif choice == '3':
            A = read_matrix("first ")
            B = read_matrix("second ")
            res = A.multiply_matrix(B) if A and B else None
            if res: res.print_matrix()

        elif choice == '4':
            print("1. Main diagonal\n2. Side diagonal\n3. Vertical line\n4. Horizontal line")
            mode = int(input("Your choice: > "))
            A = read_matrix()
            if A: A.transpose(mode).print_matrix()

        elif choice == '5':
            A = read_matrix()
            if A: print(f"The result is:\n{A.determinant()}")

        elif choice == '6':
            A = read_matrix()
            if A:
                res = A.inverse()
                if res: res.print_matrix()

        elif choice == '0':
            break


if __name__ == "__main__":
    main()