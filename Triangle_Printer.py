def triangle_printer() :
    fill, empty = "/\\", " "
    rows = input('Number of Rows (>1): ')
    while not rows.isdigit() or int(rows) < 2:
        print('Unsupported Input, Retry')
        rows = input('Number of Rows: ')
    rows = int(rows)
    for block in range(rows) : print(empty * (rows - block), fill * (block + 1), sep = "")
