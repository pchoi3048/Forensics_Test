'''
Script created on 26/02/2020 by Peter for project  .....

This script imports data from sql for python analysis
'''

# Importing packages
import pandas as pd
import pyodbc

# Creating connection to db
conn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};'
                      r"Server=(LocalDb)\LocalDBDemo;"
                      'Database=Forensics_Test;'
                      'Trusted_Connection=yes;')
# creating cursor
cursor = conn.cursor()

# Reading in table
df = pd.read_sql("""
select * from [dbo].[combined_data]
""", conn)

# Analysis (Group By)
gb=df.groupby('department')

list(df.groupby('department'))

gbs=df.groupby('department').agg({'sale_value':["sum","mean"]})
gbs.to_csv(r'C:\Users\Peter A Choi\Documents\forensics end test\forensics_end_test\Output\groupby_data.csv', index=False, header=True)
