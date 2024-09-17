import sqlite3
import os 
from dotenv import load_dotenv
import pandas as pd
import matplotlib.pyplot as plt 

load_dotenv('.env')
database=os.getenv('environment_variable_database')

# Obteniendo los 10 prodcutos mas rentables. 
conn=sqlite3.connect(database)
query='''
SELECT ProductName, SUM(Price*Quantity) as Revenue 
From [OrderDetails] od
JOIN Products p ON p.ProductID= od.ProductID
GROUP BY od.ProductID
ORDER BY Revenue DESC
LIMIT 10
'''

top_prducts=pd.read_sql_query(query,conn)

print(top_prducts)

top_prducts.plot(x='ProductName',y='Revenue',kind='bar',figsize=(10,5),legend=False)
plt.title('10 Productos mas rentables')
plt.ylabel('Revenue')
plt.ylabel('Product Name')
plt.xticks(rotation=90)
plt.show()

# Obteniendo los 10 empleados más efectivos. 

query2='''
SELECT FirstName || " " || LastName as Employee, count(*) as Total
FROM [Orders] o
Join Employees e ON e.EmployeeID= o.EmployeeID
GROUP BY o.EmployeeID
ORDER BY Total DESC 
LIMIT 10 
'''

top_employees=pd.read_sql_query(query2,conn)

top_employees.plot(x='Employee', y='Total', kind='bar',figsize=(10,5),legend=False )
plt.title('10 Mejores empleados')
plt.xlabel('Empleados')
plt.ylabel('Total_vendido')
plt.xticks(rotation=45)
plt.show()

top_employees