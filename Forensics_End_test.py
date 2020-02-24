import pandas as pd
import pyodbc
conn = pyodbc.connect('Driver={ODBC Driver 13 for SQL Server};'
                      r"Server=(LocalDb)\LocalDBDemo;"
                      'Database=Forensics_Test;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()

sql_command = pd.read_sql("""with cast_table as (
Select emp_id,
cast(number_of_sales as float) as sale_number,
cast(value_of_sales as float) as sale_value
from employee_sales
), joint as(
Select d.emp_id,
d.department,
d.location,
c.sale_number,
c.sale_value
from employee_details d
Left join cast_table c
on d.emp_id = c.emp_id
) Select 
department,
sum(sale_number) as total_number_of_sales,
sum(sale_value) as total_sales
from joint
group by department
""", conn)
df = pd.DataFrame(sql_command, columns=['department', 'total_number_of_sales', 'total_sales'])
df.to_csv(r'C:\Users\Peter A Choi\Documents\projects\export_data.csv', index=False, header=True)
print(df)
