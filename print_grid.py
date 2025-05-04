s='A B C D E F G H I'
def print_grid(matrix):
    rows=len(matrix)
    cols=len(matrix[0])
    len_header=2*cols-1
    print(f"   {s[:len_header]}")
    print()
    for r in range(rows):
        print(r, end='  ')
        for c in range(cols):
            print(matrix[r][c], end=' ')
        print()
    print("\n\n")
