def table_setup():
    '''Get: Number Of Columns, and Each Column Name(case sensative)'''
    try:
        userNumOfColumns = abs(int(input('# of columns in table: ')))
    except ValueError:
        print("Intergers only!")
        table_setup()
        
    col_nums = 1
    columns = []
    while col_nums <= userNumOfColumns:
        tableColumnName = input(f"Column {col_nums} Name: ")
        columns.append(tableColumnName)
        col_nums += 1

    return columns
