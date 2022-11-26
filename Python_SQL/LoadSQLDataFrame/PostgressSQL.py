# Libraires
import pandas as pd
import sqlalchemy as alSQL
import psycopg2 as pg
import os

#  Use enviromental variables to get password
password = os.environ.get('PSW', 'No Value')

# create the engine needed to connect Post gress to python
engine = alSQL.create_engine(f"postgresql+psycopg2://postgres:{password}@localhost:5432/postgres")

# read in the file
from sqlalchemy.sql import text
sql = """
SELECT * FROM test
"""
with engine.connect().execution_options(autocommit=True) as conn:
    query = conn.execute(text(sql))
df = pd.DataFrame(query.fetchall())
