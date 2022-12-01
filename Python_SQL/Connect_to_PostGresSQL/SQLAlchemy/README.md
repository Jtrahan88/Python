# ![#1589F0](https://placehold.co/15x15/1589F0/1589F0.png) `Send in a CSV file into a database without a table being pre-made` 

 
### Goal: Send CSV to PostgresSQL.   

#### Learning objectives:
# libraries 

    import pandas as pd
    import os
    import psycopg2 as pg
    from sqlalchemy  import create_engine

 

# Use environmental Variable to get your password
    password = os.environ.get('PSW')

   

 # create our engine
    engine = create_engine(f"postgresql+psycopg2://postgres:{password}@localhost:5432/postgres")

# The break down of engine requirements:
* engine = create_engine(dialect+driver://username:password@host:port/database)
### Break Down   
 > * postgresql+psycopg2 = dialect+driver
 > * postgres = username
 > * password = password from my environmental variable. You can type in password if needed but not recommended
 > * localhost = host
 > * 5432 = port
 > * postgres = database
    
# Get your CSV file path, I had to use an encoding aspect. reason why can be found [Here](https://stackoverflow.com/questions/22216076/unicodedecodeerror-utf8-codec-cant-decode-byte-0xa5-in-position-0-invalid-s)
    data = pd.read_csv(r"path, encoding= 'unicode_escape')
    
# Send data to Postgress SQL:
    data.to_sql('test', engine, if_exists='replace')

### Break Down
 > * test = table name you want table to be
 > * engine = engine created above. AKA our connection
 > * if_exsists = will replace old table if there. Use this with caution. 

# All Together:

    import pandas as pd
    import os
    import psycopg2 as pg
    from sqlalchemy  import create_engine
    
    password = os.environ.get('PSW')
    
    engine = create_engine(f"postgresql+psycopg2://postgres:{password}@localhost:5432/postgres")
    
    data = pd.read_csv(r"path, encoding= 'unicode_escape')
    data.to_sql('test', engine, if_exists='replace')

