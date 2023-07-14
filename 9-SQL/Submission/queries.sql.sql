-- Salary by Employee
Select  emp.emp_no,
        emp.last_name,
        emp.first_name,
        emp.sex,
        sal.salary
From employees as emp
    Left Join salaries as sal
    On (emp.emp_no = sal.emp_no)
Order By emp.emp_no;

-- Employees Who Were Hired in 1986
Select first_name, last_name, hire_date
From employees
Where hire_date between '1986-01-01' and '1986-12-31';

-- Manager of Each Derpartment
Select  dm.dept_no,
        d.dept_name,
        dm.emp_no,
        e.last_name,
        e.first_name
From dept_manager as dm
    Inner Join departments as d
        On (dm.dept_no = d.dept_no)
    Inner Join employees as e
        On (dm.emp_no = e.emp_no);

-- Department Number of Each Employee
Select  e.emp_no,
        e.last_name,
        e.first_name,
        d.dept_name
FROM employees As e
    INNER JOIN dept_emp As de
        On (e.emp_no = de.emp_no)
    INNER JOIN departments As d
        On (de.dept_no = d.dept_no)
ORDER BY e.emp_no;

-- Employees Whose First Name is "Hercules" and Last Name Starts With the Letter "B"
SELECT first_name, last_name, birth_date, sex
FROM employees
WHERE first_name = 'Hercules'
AND last_name LIKE 'B%';

-- Employees in The Sales Department
SELECT  e.emp_no,
        e.last_name,
        e.first_name,
        d.dept_name
FROM employees AS e
    INNER JOIN dept_emp AS de
        ON (e.emp_no = de.emp_no)
    INNER JOIN departments AS d
        ON (de.dept_no = d.dept_no)
WHERE d.dept_name = 'Sales'
ORDER BY e.emp_no;

-- Employees in Sales and Development Departments
SELECT  e.emp_no,
        e.last_name,
        e.first_name,
        d.dept_name
FROM employees AS e
    INNER JOIN dept_emp AS de
        ON (e.emp_no = de.emp_no)
    INNER JOIN departments AS d
        ON (de.dept_no = d.dept_no)
WHERE d.dept_name IN ('Sales', 'Development')
ORDER BY e.emp_no;

-- Frequency Count of Employees Last Names
SELECT last_name, COUNT(last_name)
FROM employees
GROUP BY last_name
ORDER BY COUNT(last_name) DESC;
