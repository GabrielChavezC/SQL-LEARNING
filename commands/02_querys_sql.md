# Database Examples/Northwind

https://en.wikiversity.org/wiki/Database_Examples/Northwind

# Querys

# AS & ORDER BY & DISTINCT

---

### AS

La cláusula `as` es para darle un alias o nombre más descriptivo a al campo.

```sql
SELECT  FirstName as nombre, LastName as apellido
FROM Employees

--> Como podemos ver le damos un nombre mas descriptivo a la tabla por ejemplo LastName --> Apellido.
--> Podemos dar la secuencia o orden que sea más util.
-->Esto no modifica la tabla original
```

| Nombre | Apellido  |
| ------ | --------- |
| Nancy  | Davolio   |
| Andrew | Fuller    |
| Janet  | Leverling |

### ORDER BY

La cláusula `ORDER BY` nos permite utilizar diferentes filtros para ordenar ya sea de manera ascendente o descendente.

```sql
SELECT  FirstName as nombre, LastName as apellido
FROM Employees



--> Por defecto ordena de mandera ASC (menor a mayor).
```

Puedes agregar `ASC` O `DESC` para odenarlos

```sql
SELECT  FirstName as nombre, LastName as apellido
FROM Employees DESC

```

| ProductID | ProductName        | SupplierID | Category | Unit             | Price |
| --------- | ------------------ | ---------- | -------- | ---------------- | ----- |
| 33        | Geitost            | 15         | 4        | 500 g            | 2.5   |
| 24        | Guaraná Fantástica | 10         | 1        | 12 - 355 ml cans | 4.5   |
| 13        | Konbu              | 6          | 8        | 2 kg box         | 6     |

Que sucede si ordenamos por ProductName o campo texto.

El orden se maneja de esta manera de manera asc y viceversa para desc

1. null " "
2. números 1 2 3
3. caracteres especiales /() . ,
4. letras a b c

| ProductID | ProductName       | SupplierID | Category | Unit                | Price |
| --------- | ----------------- | ---------- | -------- | ------------------- | ----- |
| 17        | Alice Mutton      | 7          | 6        | 20 - 1 kg tins      | 39    |
| 3         | Aniseed Syrup     | 1          | 2        | 12 - 550 ml bottles | 10    |
| 40        | Boston Crab Meat  | 19         | 8        | 24 - 4 oz tins      | 18.4  |
| 60        | Camembert Pierrot | 28         | 4        | 15 - 300 g rounds   | 34    |

### DISTINCT

La cláusula `DISTINCT` nos da los valores únicos de algun campo.

```sql
SELECT DISTINCT ProductName
FROM Products
--> DISTINCT se utiliza después del SELECT
```

# WHERE

---

La cláusula `WHERE` se utiliza para filtrar registros.

```sql
SELECT * FROM Products
WHERE ProductID=14
```

| ProductID | ProductName | SupplierID | Category | Unit             | Price |
| --------- | ----------- | ---------- | -------- | ---------------- | ----- |
| 14        | Tofu        | 6          | 7        | 40 - 100 g pkgs. | 23.25 |

Otras

```sql
SELECT * FROM Products
WHERE price>40
--> Productos mayores a 40

SELECT ProductName FROM Products
WHERE price>40
--> Solo el nombre del producto mayores a 40

```

## DELETE WHERE

> [!WARNING]  
> Un DELETE dbe estar acompañado de un where.

> Si omites el WHERE, todos los registros en la tabla serán eliminados!

Un `DELETE` acompaños con un where para referirnos que campo vamos a eliminar.

```sql
DELETE FROM Products
WHERE ProductID=77
```

## UPDATE WHERE

`UPDATE` podemos hacer la modificación de un registro espacificando uno o más campos.

```sql
UPDATE Products SET Price=12,ProductName='chesse'
WHERE ProductID = 1
```

# AND, OR & NOT

### AND

La cláusula `AND` se utiliza para filtrar resgitros de una o más condiciones.

```sql
SELECT * FROM Customers
WHERE CustomerID>=50 AND CustomerID<55
```

| CustomerID | CustomerName           | ContactName     | Address                             | City         | PostalCode | Country   |
| ---------- | ---------------------- | --------------- | ----------------------------------- | ------------ | ---------- | --------- |
| 50         | Maison Dewey           | Catherine Dewey | Rue Joseph-Bens 532                 | Bruxelles    | B-1180     | Belgium   |
| 51         | Mère Paillarde         | Jean Fresnière  | 43 rue St. Laurent                  | Montréal     | H1J 1C3    | Canada    |
| 52         | Morgenstern Gesundkost | Alexander Feuer | Heerstr. 22                         | Leipzig      | 4179       | Germany   |
| 53         | North/South            | Simon Crowther  | South House 300 Queensbridge        | London       | SW7 1RZ    | UK        |
| 54         | Océano Atlántico Ltda. | Yvonne Moncada  | Ing. Gustavo Moncada 8585 Piso 20-A | Buenos Aires | 1010       | Argentina |

### OR

La cláusula `OR` se utiliza para filtrar los registros de más de una condición, si se cumple una u otra condición.

```sql
SELECT * FROM Employees
WHERE FirstName='Nancy' OR FirstName='Anne'
```

| EmployeeID | LastName  | FirstName | BirthDate  | Photo      | Notes                                                                 |
| ---------- | --------- | --------- | ---------- | ---------- | --------------------------------------------------------------------- |
| 1          | Davolio   | Nancy     | 1968-12-08 | EmpID1.pic | Education includes a BA in psychology from Colorado State University. |
| 9          | Dodsworth | Anne      | 1969-07-02 | EmpID9.pic | Anne has a BA degree in English from St. Lawrence College.            |

> [!TIP]
> Puedes usar los dos Operadores AND Y OR

```sql
SELECT * FROM Products
WHERE (Price<20 OR CategoryID=6) AND SupplierID=7

-->Tenemos que el precio sea menor a 20 O categoría sea 6, donde solo tengamos el proveedor 7
```

| ProductID | ProductName   | SupplierID | Category | Unit                | Price |
| --------- | ------------- | ---------- | -------- | ------------------- | ----- |
| 16        | Pavlova       | 7          | 3        | 32 - 500 g boxes    | 17.45 |
| 17        | Alice Mutton  | 7          | 6        | 20 - 1 kg tins      | 39    |
| 70        | Outback Lager | 7          | 1        | 24 - 355 ml bottles | 15    |

### NOT

La cláusula `NOT` niega la condición.

```sql
SELECT * FROM Products
WHERE NOT Price >40
-->Donde no tengamos productos con precio mayor a 40."NO ME MUESTRES PRECIOS MAYORES A 40"
```

| ProductID | ProductName   | SupplierID | Category | Unit                | Price |
| --------- | ------------- | ---------- | -------- | ------------------- | ----- |
| 1         | Chais         | 1          | 1        | 10 boxes x 20 bags  | 18    |
| 2         | Chang         | 1          | 1        | 24 - 12 oz bottles  | 19    |
| 3         | Aniseed Syrup | 1          | 2        | 12 - 550 ml bottles | 10    |

# LIMIT

### LIMIT

La cláusula `LIMIT` nos limita los registros a mostrar.

```sql
SELECT * FROM Customers
WHERE CustomerID>=40
AND NOT Country='Germany'
LIMIT 5
--> Solo me muestra 5 registros.
--------------------------------------
--> Podemos hacer muestras aleatorias con Random()
SELECT * FROM Customers
WHERE CustomerID>=40
AND NOT Country='Germany'
ORDER BY RANDOM()
LIMIT 5
--> Solo me muestra 5 registros.
```

| CustomerID | CustomerName                  | ContactName     | Address                | City          | PostalCode | Country |
| ---------- | ----------------------------- | --------------- | ---------------------- | ------------- | ---------- | ------- |
| 40         | La corne d'abondance          | Daniel Tonini   | 67, avenue de l'Europe | Versailles    | 78000      | France  |
| 41         | La maison d'Asie              | Annette Roulet  | 1 rue Alsace-Lorraine  | Toulouse      | 31000      | France  |
| 42         | Laughing Bacchus Wine Cellars | Yoshi Tannamuri | 1900 Oak St.           | Vancouver     | V3F 2K1    | Canada  |
| 43         | Lazy K Kountry Store          | John Steel      | 12 Orchestra Terrace   | Walla Walla   | 99362      | USA     |
| 45         | Let's Stop N Shop             | Jaime Yorres    | 87 Polk St. Suite 5    | San Francisco | 94117      | USA     |

# BETWEEN, LIKE, IN, NOT IN

### BETWEEN

El operador `BETWEEN` selecciona valores dentro de un rango dado.

```sql

SELECT * FROM Products
WHERE Price BETWEEN 20 and 40
-------------------------------------
--> Operador AND
SELECT * FROM Products
WHERE Price>20 and Price<40

```

| ProductID | ProductName                     | SupplierID | Category | Unit            | Price |
| --------- | ------------------------------- | ---------- | -------- | --------------- | ----- |
| 4         | Chef Anton's Cajun Seasoning    | 2          | 2        | 48 - 6 oz jars  | 22    |
| 5         | Chef Anton's Gumbo Mix          | 2          | 2        | 36 boxes        | 21.35 |
| 6         | Grandma's Boysenberry Spread    | 3          | 2        | 12 - 8 oz jars  | 25    |
| 7         | Uncle Bob's Organic Dried Pears | 3          | 7        | 12 - 1 lb pkgs. | 30    |

El operador `BETWEEN` también selecciona un rango fechas.

```sql
SELECT * FROM Employees
WHERE BirthDate
BETWEEN '1960-0-1' AND '1970-0-1'

```

### LIKE

El operador `LIKE` se utiliza en un WHERE para buscar un patrón especificado en una columna.

```sql
SELECT * FROM Employees
WHERE LastName LIKE 'FULLER'
```

| EmployeeID | LastName | FirstName | BirthDate  | Photo      | Notes                      |
| ---------- | -------- | --------- | ---------- | ---------- | -------------------------- |
| 2          | Fuller   | Andrew    | 1952-02-19 | EmpID2.pic | Andrew received his BTS .. |

El operador `LIKE` podemos agregar el símbolo `% `para que antes busque antes o después sobre la letra proporcionada.

```sql
SELECT * FROM Employees
WHERE LastName LIKE 'F%'
```

| EmployeeID | LastName | FirstName | BirthDate  | Photo      | Notes                      |
| ---------- | -------- | --------- | ---------- | ---------- | -------------------------- |
| 2          | Fuller   | Andrew    | 1952-02-19 | EmpID2.pic | Andrew received his BTS .. |

Podemos realizar una consulta mientras el texto contenga una `%r%` muestre los registros. Con dos porcentajes.

```sql
SELECT * FROM Employees
WHERE LastName LIKE '%r%'

```

LIKE VERIFICA

- Una cadena empiece con algo.
- Una cadena termine con algo.
- Una cadena contenga algo.

### IN

El operador `IN` permite especificar múltiples valores en un WHERE cláusula.

```sql
SELECT * FROM Products
WHERE SupplierID IN (3,4,6)
```

| ProductID | ProductName                     | SupplierID | Category | Unit                | Price |
| --------- | ------------------------------- | ---------- | -------- | ------------------- | ----- |
| 6         | Grandma's Boysenberry Spread    | 3          | 2        | 12 - 8 oz jars      | 25    |
| 7         | Uncle Bob's Organic Dried Pears | 3          | 7        | 12 - 1 lb pkgs.     | 30    |
| 8         | Northwoods Cranberry Sauce      | 3          | 2        | 12 - 12 oz jars     | 40    |
| 9         | Mishi Kobe Niku                 | 4          | 6        | 18 - 500 g pkgs.    | 97    |
| 10        | Ikura                           | 4          | 8        | 12 - 200 ml jars    | 31    |
| 13        | Konbu                           | 6          | 8        | 2 kg box            | 6     |
| 14        | Tofu                            | 6          | 7        | 40 - 100 g pkgs.    | 23.25 |
| 15        | Genen Shouyu                    | 6          | 2        | 24 - 250 ml bottles | 15.5  |
| 74        | Longlife Tofu                   | 4          | 7        | 5 kg pkg.           | 10    |

El operador `NOT IN` niega la condición donde no deben de encontrarse esos valores.

```sql
SELECT * FROM Products
WHERE SupplierID NOT IN (3,4,6)
```

# Funciones de Agregación

---

Una función agregada es una función que realiza un cálculo en un conjunto de valores y devuelve un solo valor.

- MIN()- devuelve el valor más pequeño dentro de la columna seleccionada.

- MAX()- devuelve el mayor valor dentro de la columna seleccionada.

- COUNT()- devuelve el número de filas en un conjunto.

- SUM()- devuelve la suma total de a columna numérica.

- AVG()- devuelve el valor promedio de a columna numérica.

Las funciones agregadas ignoran los valores nulos (excepto para COUNT()).

```sql
SELECT count(FirstName)
From Employees
```

| count(FirstName) |
| ---------------- |
| 10               |

```sql
SELECT ROUND(AVG(Price)) AS 'Promedio'
From Products
--> Podemos agregar mas funciones y agregandoles un alías.

SELECT ROUND(AVG(Price),2) AS 'Promedio'
From Products
--> Podemos delimitar los decimales a mostrar.
```

| Promedio |
| -------- |
| 29.0     |

# Group by & Having

---

## GROUP BY

El `GROUP BY` agrupa las filas que tienen los mismos valores en resumen filas.

```sql
SELECT ProductName,SUM(Price) AS total FROM  Products
GROUP BY ProductName
ORDER BY total
```

| ProductName        | total |
| ------------------ | ----- |
| Geitost            | 2.5   |
| Guaraná Fantástica | 4.5   |
| Konbu              | 6     |
| Filo Mix           | 7     |

> [!CAUTION]
> No podemos utilizar una funcion de agregación en un where para hacer un filtro.

```sql
SELECT ProductName,SUM(Price) AS total FROM  Products
-->No sepuede hacer esto
WHERE total>30
GROUP BY ProductName
ORDER BY total

```

El `GROUP BY` NO PUEDE UTILIZAR UN WHERE CON UNA FUNCION DE AGREGACION, en este caso _total_ para estos casos utilizamos **HAVING**.

## HAVING

El `HAVING` cláusula se agregó a SQL porque el WHERE la palabra clave no puede ser utilizado con funciones agregadas.

```sql
SELECT ProductName,SUM(Price) AS total FROM  Products
GROUP BY ProductName
HAVING total>40
ORDER BY total
```

| ProductName        | Total |
| ------------------ | ----- |
| Schoggi Schokolade | 43.9  |
| Vegie-spread       | 43.9  |
| Rössle Sauerkraut  | 45.6  |
| Ipoh Coffee        | 46    |

> [!IMPORTANT]  
> NO TE CONFUNDAS

Se puede utilizar eL WHERE siempre y cuando no contenga una función de agregación y se coloca antes del GROUP BY

```sql
SELECT ProductName,SUM(Price) AS total FROM  Products
WHERE ProductName LIKE 'S%'
GROUP BY ProductName
```

| ProductName         | Total |
| ------------------- | ----- |
| Sasquatch Ale       | 14    |
| Schoggi Schokolade  | 43.9  |
| Scottish Longbreads | 12.5  |

# SUBCONSULTAS

---

Una subconsulta refiere a una consulta dentro de otra consulta que permite hacer cosas mas avanzadas.

```sql
SELECT ProductID,
	Quantity,
	(SELECT ProductName
    From Products WHERE OrderDetails.ProductID=ProductID ) as Nombre
From OrderDetails
```

| ProductID | Quantity | Nombre                        |
| --------- | -------- | ----------------------------- |
| 11        | 12       | Queso Cabrales                |
| 42        | 10       | Singaporean Hokkien Fried Mee |
| 72        | 5        | Mozzarella di Giovanni        |
| 14        | 9        | Tofu                          |
| 51        | 40       | Manjimup Dried Apples         |

¿Cuáles son los productos que más recaudaron?

```sql
SELECT ProductID, SUM(Quantity) AS total_vendido,
		(SELECT Price From Products WHERE od.ProductID=ProductID) as price,
		(SELECT ProductName From Products WHERE od.ProductID=ProductID) as nombre,
		(SUM(Quantity)* (SELECT Price From Products WHERE od.ProductID=ProductID)) as Total_recaudado
FROM [OrderDetails] od
GROUP BY ProductID
ORDER BY total_recaudado DESC
LIMIT 10
```

| ProductID | Total Vendido | Price  | Nombre                  | Total Recaudado |
| --------- | ------------- | ------ | ----------------------- | --------------- |
| 38        | 239           | 263.5  | Côte de Blaye           | 62976.5         |
| 29        | 168           | 123.79 | Thüringer Rostbratwurst | 20796.72        |
| 59        | 346           | 55     | Raclette Courdavault    | 19030           |
| 62        | 325           | 49.3   | Tarte au sucre          | 16022.5         |

¿Cuáles son los empleados que vendieron más que el promedio?

```sql
SELECT FirstName, LastName,
(
	SELECT SUM(od.Quantity) FROM [Orders] o, [OrderDetails] od
	WHERE o.EmployeeID=e.EmployeeID AND od.OrderID=o.OrderID
) as unidades_totales

FROM [Employees] e
WHERE unidades_totales < (select AVG(unidades_totales) FROM (
SELECT(SELECT SUM(od.Quantity) FROM [Orders] o, [OrderDetails] od
	WHERE o.EmployeeID=e2.EmployeeID AND od.OrderID=o.OrderID) as unidades_totales FROM [Employees] e2
GROUP BY e2.EmployeeID
))

```

| FirstName | LastName  | Unidades Totales |
| --------- | --------- | ---------------- |
| Nancy     | Davolio   | 1924             |
| Janet     | Leverling | 1725             |
| Margaret  | Peacock   | 3232             |

# JOINS

---

La cláusula `JOIN` se utiliza para combinar filas de dos o más tablas, basado en una columna relacionada entre ellos.

## INNER JOIN

Selecciona registros que tienen valores coincidentes en ambas tablas.

```sql
SELECT * FROM Employees e, 	Orders o
WHERE e.EmployeeID=O.EmployeeID
```

```sql
SELECT * FROM [Employees] e
INNER JOIN [Orders] o ON e.EmployeeID=o.EmployeeID
```
