#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
import datetime
import psycopg2
import os


# In[ ]:


def connectPostGres(dataframe):
    """Will send data frame to postgress SQL premade database"""
    conn = None
    cur = None
    global hostName, database, username, pwd, port_id
    global columns

    # What table name to we want
    tablename = input('Table name in SQL: ')

    # fuction will allow to assign a varables to SQL sever so not to repeat every time
    SQL_sever_needed = input("SQL hostname/etc needed?: 'Y' or 'N' ").lower()
    if SQL_sever_needed == 'y' or SQL_sever_needed == 'yes':
        hostName, database, username, pwd, port_id = SQL_hosting()
    else:
        pass
    # get number of columns and column names
    columns = table_setup()

    # Alter Dataframe for only columns needed
    dataframe = dataframe[columns]

    # convert values to a list of tuples
    dataframeTupleList = list(dataframe.itertuples(index=False, name=None))

    # get number of value columns to be entered in SQL
    num_col_values = ("%s," * len(dataframe.columns))[:-1]

    # try except final for errors
    try:
        conn = psycopg2.connect(
            host=hostName,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id)

        # create writing scripts
        cur = conn.cursor()

        # drops table to insert all new data(complete overwrite of old data):*************************************************Can take out if needed
        cur.execute(f"DROP TABLE IF EXISTS {tablename}")

        # columns + " " + datatype for our creat table script
        datatype = []
        for i in range(len(columns)):
            datatype.append(columns[i] + " " + input(f"Data Type for {columns[i]} in SQL syntax: "))
        datatype = ", ".join([i for i in datatype])

        # create our table in the database
        create_script = f""" CREATE TABLE IF NOT EXISTS {tablename}({datatype})"""

        cur.execute(create_script)

        # take of the ' ' in the column names
        columns = ", ".join([i for i in columns])

        # insert table values into excel
        insert_script = f'INSERT INTO {tablename} ({columns}) VALUES({num_col_values})'
        for value in dataframeTupleList:
            cur.execute(insert_script, value)

        # save teh transaction into SQL
        conn.commit()
        print('\nSQL has been updated!')
    except Exception as error:
        print(error)
    finally:
        conn.close()
        cur.close()


# In[ ]:


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


# In[ ]:


def table_setup():
    '''Get: Number Of Columns, and Each Column Name(case sensative)'''
    userNumOfColumns = int(input('# of columns in table: '))
    col_nums = 1
    columns = []
    while col_nums <= userNumOfColumns:
        tableColumnName = input(f"Column {col_nums} Name: ")
        columns.append(tableColumnName)
        col_nums += 1

    return columns

