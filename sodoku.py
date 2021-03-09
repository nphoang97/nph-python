class _Case:

    def __init__(self):
        self.case = {}

    case = {}

    def add_case():
        return

    def has_next_case():
        return has_back_cell() or has_up_cell() or has_forward_cell()

    def gen_next_case():
        if has_forward_cell():
            return forward_cell()
        if has_up_cell():
            return up_cell()
        if has_back_cell():
            return back_cell()

    def back_cell():
        return

    def has_back_cell():
        return

    def up_cell():
        return

    def has_up_cell():
        return

    def forward_cell():
        return

    def has_forward_cell():
        return

    def print_case():
        print(case)

class SodokuSolver:

    sodoku_box = [[0]*9]*9

    case = {}

    def __init__(self):
        super().__init__()
        self.case = _Case()

    def input_sodoku(self):
        for row in range(1, 11):
            for col in range(1, 11):
                value = int(input())
                self.case.case[row][col] = value
                if value == 0:
                    self.case.add_case(row, col, value)
        self.case.print_case()
        print("wait")

    # gen all case and return first sastify case, if not any case is sastify return null
    def solve():
        while (not check_sodoku()) and case.has_next_case:
            case.gen_next_case()
        return

    def check_sodoku():
        return

    def check_row(row_position):
        return

    def check_col(col_position):
        return

    def check_box(box_position):
        return  

    def print_solution():
        return


def main():
    sodoku_solver = SodokuSolver()
    sodoku_solver.input_sodoku()
    sodoku_solver.solve()
    sodoku_solver.print_solution()

if __name__ == '__main__':
    main()