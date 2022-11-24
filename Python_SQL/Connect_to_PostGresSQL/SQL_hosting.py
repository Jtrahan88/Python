def SQL_hosting():
    '''Get: hostName, database, username, pwd, port_id'''
    # fuction will allow to assogn a varable to SQL sever
    print('Following data is needed:\n')
    hostName = input('hostName: ')
    username = input('username: ')
    pwd = os.environ.get('PSW')
    port_id = input('Port ID: ')
    database = input('database name: ')
    
    return hostName, database, username, pwd, port_id
