# Write your MySQL query statement below
Select e.employee_id
from Employees e

Left Join Employees m on e.manager_id = m.employee_id
where e.salary  < 30000
 AND e.manager_id is NOT NULL
 AND m.employee_id is NULL
Order by e.employee_id;