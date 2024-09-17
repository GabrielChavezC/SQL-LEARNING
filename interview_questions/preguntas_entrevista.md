# Preguntas de entevista

# 1. ¿Qué diferencia hay entre `DISTINTO` y `NOT`? (=! & NOT)

---

La cláusula `NOT` es un operador Booleano/lógico y distinto de es un operador de comparación `=!`

```sql
-->Distinto
SELECT * FROM Customers
WHERE  Country!='USA'
LIMIT 5
----------------------
-->NOT
SELECT * FROM Customers
WHERE NOT Country='USA'
LIMIT 5

```

    - Aunque nos den el mismo resultado, el funcinamiento es distinto.

# 2. ¿Qué diferencia hay entre `GROUP BY` y `HAVING`?

---

El `HAVING` cláusula se agregó a SQL porque el `WHERE` la palabra clave no puede ser utilizado con funciones agregadas.

```sql
-->CORRECTO
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

```sql
-->INCORRECTO
SELECT ProductName,SUM(Price) AS total FROM  Products
-->No sepuede hacer esto
WHERE total>30
GROUP BY ProductName
ORDER BY total
```

# 3. ¿Qué diferencia hay entre `ALTER` y `DROP`?

---

Alter

Propósito: Se utiliza para modificar la estructura de una tabla existente sin eliminarla.

```sql
ALTER TABLE empleados ADD columna_nueva VARCHAR(50);
```

DROP

Propósito: Se utiliza para eliminar por completo tablas, bases de datos o columnas.

```sql
DROP TABLE empleados;
```

- ALTER modifica la estructura de un objeto sin eliminarlo.

- DROP elimina un objeto por completo, junto con sus datos (si es una tabla o base de datos).
