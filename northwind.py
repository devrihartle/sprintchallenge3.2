import sqlite3

# create a connection
conn = sqlite3.connect('northwind_small.sqlite3')

# create a cursor
curs = conn.cursor()

# query to find 10 most expensive items in the database
expensive_items = """
SELECT *
FROM Product
ORDER BY UnitPrice DESC
LIMIT 10;
"""

# query to find average age of an employee at hire time
avg_hire_age = """
SELECT avg(HireDate-Employee.BirthDate)
as avg_age
FROM Employee;
"""

# query to find average age by city
avg_age_by_city = """SELECT city, avg(HireDate - Employee.BirthDate)
as average_age 
FROM Employee 
GROUP BY City;
"""

# query to find ten most expensive AND suppliers
ten_most_expensive = """
SELECT *
FROM Product
LEFT JOIN Supplier 
ON Product.SupplierID = Supplier.SupplierID
ORDER BY UnitPrice DESC
LIMIT 10;
"""

# query to find largest category
largest_category = """
SELECT CategoryName, max(frequency)
FROM (SELECT CategoryName, count(CategoryName)
as frequency 
FROM (SELECT * FROM Product
LEFT JOIN Category ON Product.CategoryId = Category.Id)
group by CategoryName);
"""
