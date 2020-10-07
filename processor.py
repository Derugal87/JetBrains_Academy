from numpy import array
from numpy import dot
from numpy import linalg


class Matrices:

    def __init__(self):
        self.mx = None
        self.second_mx = None
        self.final_mx = None
        self.size = None
        self.second_size = None

    def prepare_two_data(self):
        self.size = input('Enter size of first matrix: ').split(' ')
        self.size = [int(i) for i in self.size]

        print('Enter first matrix: ')
        self.mx = [input('').split() for _ in range(self.size[0])]
        if self.mx[0][0].replace('-', '', 1).isdigit():
            self.mx = [[int(i) for i in row] for row in self.mx]
        elif self.mx[0][0].replace('.', '', 1).replace('-', '', 1).isdigit():
            self.mx = [[float(i) for i in row] for row in self.mx]

        self.second_size = input('Enter size of second matrix: ').split(' ')
        self.second_size = [int(i) for i in self.second_size]

        print('Enter second matrix: ')
        self.second_mx = [input('').split() for _ in range(self.second_size[0])]
        if self.second_mx[0][0].replace('-', '', 1).isdigit():
            self.second_mx = [[int(i) for i in row] for row in self.second_mx]
        elif self.second_mx[0][0].replace('.', '', 1).replace('-', '', 1).isdigit():
            self.second_mx = [[float(i) for i in row] for row in self.second_mx]

        return self.size, self.mx, self.second_size, self.second_mx

    def prepare_one_data(self):
        self.size = input('Enter size of matrix: ').split(' ')
        self.size = [int(i) for i in self.size]

        print('Enter matrix: ')
        self.mx = [input('').split() for _ in range(self.size[0])]
        if self.mx[0][0].replace('-', '', 1).isdigit():
            for row in self.mx:
                for i in row:
                    if '.' in i:
                        self.mx = [[i.split('.')[0] for i in row] for row in self.mx]
            self.mx = [[int(i) for i in row] for row in self.mx]
        elif self.mx[0][0].replace('.', '', 1).replace('-', '', 1).isdigit():
            self.mx = [[float(i) for i in row] for row in self.mx]

        return self.size, self.mx

    def print_matrices(self):
        print('The result is: ')
        for row in self.final_mx:
            print(' '.join(map(str, row)))
        print()
        self.run()

    def add_matrices(self):
        self.prepare_two_data()

        self.final_mx = []
        # for i in range(self.size[0]):
        #     self.final_mx.append([0] * self.size[1])

        if self.size == self.second_size:
            self.mx = array(self.mx)
            self.second_mx = array(self.second_mx)
            self.final_mx = self.mx + self.second_mx
            self.print_matrices()
        else:
            print('The operation cannot be performed.\n')
            self.run()

    def const_multiply(self):
        self.prepare_one_data()

        const = input('Enter constant: ')
        if const.replace('-', '', 1).isdigit():
            const = int(const)
        elif const.replace('.', '', 1).replace('-', '', 1).isdigit():
            const = float(const)

        self.final_mx = [[elem * const for elem in row] for row in self.mx]
        self.print_matrices()

    def multiply_matrices(self):
        self.prepare_two_data()

        self.final_mx = []

        if self.size[1] == self.second_size[0]:
            self.final_mx = dot(self.mx, self.second_mx)
            self.print_matrices()
        else:
            print('The operation cannot be performed.\n')
            self.run()

    def transpose_matrix_menu(self):
        print(f'\n1. Main diagonal\n'
              f'2. Side diagonal\n'
              f'3. Vertical line\n'
              f'4. Horizontal line')
        choice = int(input('Your choice: '))
        if choice == 1:
            self.transpose_main_diagonal()
        elif choice == 2:
            self.transpose_side_diagonal()
        elif choice == 3:
            self.transpose_vertical_line()
        elif choice == 4:
            self.transpose_horizontal_line()
        elif choice == 0:
            exit(0)
        else:
            print('Choose right point')
            self.transpose_matrix_menu()

    def transpose_main_diagonal(self):
        self.prepare_one_data()
        self.mx = array(self.mx)
        self.final_mx = self.mx.transpose()
        self.print_matrices()

    def transpose_side_diagonal(self):
        self.prepare_one_data()
        self.mx = self.mx[::-1]
        self.mx = array(self.mx)
        self.final_mx = self.mx.transpose()
        self.final_mx = self.final_mx[::-1]
        self.print_matrices()

    def transpose_vertical_line(self):
        self.prepare_one_data()
        self.final_mx = []
        for i in self.mx:
            self.final_mx.append(i[::-1])
        self.print_matrices()

    def transpose_horizontal_line(self):
        self.prepare_one_data()
        self.final_mx = self.mx[::-1]
        self.print_matrices()

    def determinant_matrix(self):
        self.prepare_one_data()
        print('The result is: ')
        print(linalg.det(self.mx))

    def inverse_matrix(self):
        self.prepare_one_data()
        try:
            self.final_mx = linalg.inv(self.mx)
            self.print_matrices()
        except linalg.LinAlgError:
            print("This matrix doesn't have an inverse.")
            self.menu()

    def menu(self):
        print(f'1. Add matrices\n'
              f'2. Multiply matrix by a constant\n'
              f'3. Multiply matrices\n'
              f'4. Transpose matrix\n'
              f'5. Calculate a determinant\n'
              f'6. Inverse matrix\n'
              f'0. Exit')
        choice = int(input('Your choice: '))
        if choice == 1:
            self.add_matrices()
        elif choice == 2:
            self.const_multiply()
        elif choice == 3:
            self.multiply_matrices()
        elif choice == 4:
            self.transpose_matrix_menu()
        elif choice == 5:
            self.determinant_matrix()
        elif choice == 6:
            self.inverse_matrix()
        elif choice == 0:
            exit(0)
        else:
            print('Choose right point')
            self.menu()

    def run(self):
        self.menu()


if __name__ == '__main__':
    Matrices().run()
