import xlrd

if __name__ == "__main__":
    data = xlrd.open_workbook("./python-game-test/excel/test.xlsx")
    table = data.sheets()[0]
    print(table)
    table = data.sheet_by_index(0)
    print(table)
    table = data.sheet_by_name("a")
    print(table)
    names = data.sheet_names()
    print(names)
    a = data.sheet_loaded("a")
    print(a)

    nrows = table.nrows
    print(nrows)

    row_data = table.row(0)
    print(row_data)

    row_data = table.row_slice(0)
    print(row_data)

    types = table.row_values(1, start_colx=0, end_colx=1)
    print(types)

    cols = table.col(0)
    print(cols)

    cel = table.cell_value(0,0)
    print(cel)