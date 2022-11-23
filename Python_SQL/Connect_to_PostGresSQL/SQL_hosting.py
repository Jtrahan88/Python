def SQL_hosting():
    '''Get: hostName, database, username, pwd, port_id'''
    # fuction will allow to assogn a varable to SQL sever
    print('Following data is needed:\n')
    hostName = input('hostName: ')
    database = input('database name: ')
    username = input('username: ')
    pwd = input('password: ')
    port_id = input('Port ID: ')

    return hostName, database, username, pwd, port_id
