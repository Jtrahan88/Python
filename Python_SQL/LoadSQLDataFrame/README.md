# ![#1589F0](https://placehold.co/15x15/1589F0/1589F0.png) `Take in a table from PostgresSQL to a python pandas DataFrame` 

> * [Source for helping set this up](https://towardsdatascience.com/work-with-sql-in-python-using-sqlalchemy-and-pandas-cd7693def708)
 
### Goal: Load in a table from an SQL server to preform ETL on.   

#### Learning objectives:
* > The break down of engine requirments:
* > engine = create_engine(dialect+driver://username:password@host:port/database)
* > > postgresql+psycopg2 = dialect+driver
* > > postgres = username
* > > password = password from my envriomental variable. You can type in password if needed but not recommended
* > > localhost = host
* > > 5432 = port
* > > postgres = database

#### Crate a query to read into pandas:
* read in the file
* > from sqlalchemy.sql import text
* > sql = """
* > SELECT * FROM table_name
* > """
 
#### Connect and execute the query above:
* Connect and execute:
* > with engine.connect().execution_options(autocommit=True) as conn:
* >     query = conn.execute(text(sql))
* > df = pd.DataFrame(query.fetchall())
