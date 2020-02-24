use Forensics_Test
--select * from employee_details
--select * from employee_sales
;
with cast_table as (
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
