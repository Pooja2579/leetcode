CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
declare M INT;
Set M = N-1;

IF N<=0 THEN Return NULL; End if;
  RETURN (
      # Write your MySQL query statement below.
      select distinct salary from Employee order by salary desc limit 1 offset M

  );
END
