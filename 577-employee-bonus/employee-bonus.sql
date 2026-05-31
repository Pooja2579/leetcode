# Write your MySQL query statement below
select name, bonus from Employee left join Bonus on employee.empId = bonus.empId where IFNULL(bonus , 0)<1000;