from pwn import *
import z3

def solve_sudoku(instance):
    grid = [[z3.Int(f'grid_%s_%s' % (i+1, j+1)) for j in range(9)] for i in range(9)]
    s = z3.Solver()

    # Make sure each cell must contain a digit (1-9)
    cells_c = [z3.And(1 <= grid[i][j], grid[i][j] <= 9) for i in range(9) for j in range(9)]

    # Make sure every digit has to be placed exactly once in each row
    rows_c = [z3.Distinct(grid[i]) for i in range(9)]

    # Make sure every digit has to be placed exactly once in each column
    cols_c = [z3.Distinct([grid[i][j] for i in range(9)]) for j in range(9)]

    # Make sure every digit must be placed exactly once in each 3x3 subgrid
    sq_c = [z3.Distinct([ grid[3*i0 + i][3*j0 + j] for i in range(3) for j in range(3) ]) for i0 in range(3) for j0 in range(3)]

    # The main condition
    sudoku_c = cells_c + rows_c + cols_c + sq_c

    instance_c = [z3.If(instance[i][j] == 0,
                        True,
                        grid[i][j] == instance[i][j])
                  for i in range(9) for j in range(9)]

    s.add(sudoku_c + instance_c)
    if s.check() == z3.sat:
        m = s.model()
        return [[m.evaluate(grid[i][j]) for j in range(9)] for i in range(9)]

def main():
    context.log_level = 'debug'
    r = process('./sudoku_master')
    r = remote('chal.firebird.sh', 35054)
    instance = [[0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0],
                [0,0,0,0,0,0,0,0,0]]

    for i in range(30):
        r.recvuntil(b':\n')
        for h in range(9):
            line = r.recvline()
            for k in range(9):
                char = chr(line[k*3])
                instance[h][k] = int(char) if char != '.' else 0
        solution = solve_sudoku(instance)
        r.recvuntil(b'Please enter the solution in one line: ')
        r.sendline(''.join([str(solution[i][j]) for i in range(9) for j in range(9)]))
    r.interactive()

if __name__ == '__main__':
    main()