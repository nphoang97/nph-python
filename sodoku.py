
sodoku_box = [[0]*9]*9
case = {
    'abc': '123',
    123: 456
}

def main():
    input_sodoku()
    solve()
    print_solution()
    return

if __name__ == '__main__':
    main()

def input_sodoku():
    init_case()
    return

def init_case():
    return

# gen all case and return first sastify case, if not any case is sastify return null
def solve():
    while (not check_sodoku()) and has_next_case():
        gen_next_case()
    return

def has_next_case():
    return

def gen_next_case():
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

