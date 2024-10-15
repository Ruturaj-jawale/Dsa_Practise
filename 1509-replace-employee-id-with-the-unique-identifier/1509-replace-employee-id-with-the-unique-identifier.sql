# Write your MySQL query statement below
SELECT 
EmployeeUNI.unique_id,Employees.name
From Employees
LEFT JOIN EmployeeUNI on Employees.id = EmployeeUNI.id