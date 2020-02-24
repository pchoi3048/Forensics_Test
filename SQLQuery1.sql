use Forensics_Test
--select * from employee_details
--select * from employee_sales
;
with joint as (
Select d.emp_id,
		d.department,
		d.location,
		s.number_of_sales,
		s.value_of_sales
from employee_details d
Left join employee_sales s
on d.emp_id = s.emp_id
)Select
		*
from joint

	