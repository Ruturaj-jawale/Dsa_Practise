CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  Set N = N - 1;
  RETURN (
     SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 1 OFFSET N
  );
END