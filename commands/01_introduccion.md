consulta para la creacion de una base de datos

```sql
CREATE DATABASE "usuarios"

USE DATABASE usuarios
```

Sentecnia para crear una tabla en una base de datos

```sql
CREATE TABLE "usuarios" (
    "nombre"    TEXT,
    "apellido"  TEXT,
    "edad"      INTEGER
);
```

Una consulta es una petición o busqueda en la base de datos, para obtener información.

Selección completa de alguna tabla.

```sql
SELECT * FROM "usuarios"

-->El Símbolo (*) hace una selección completa en nuestra consulta.
```

| nombre | apellido | edad    |
| ------ | -------- | ------- |
| TEXT   | TEXT     | INTEGER |

Inserción de valores a una tabla.

```sql
INSERT INTO usuarios (nombre,apellido,edad)
VALUES  ('Ramon','Juarez',21),
        ('Fernando','Solis',25)

 -->Una inserción de mas datos se puede separar por una coma (,)
```

| nombre   | apellido | edad |
| -------- | -------- | ---- |
| Ramon    | Juarez   | 21   |
| Fernando | Solis    | 25   |

Consulta sobre una selección de campos especificos especifica

```sql
SELECT nombre FROM usuarios

 -->Se pueden seleccionar uno, dos o más campos (nomnbre,apellido).
```

`Todos los SELECT nos devuelven una Tabla`

| nombre   |
| -------- |
| Ramon    |
| Fernando |

# Identificadores

## Clave Primaria (Primary Key)

Una clave primaria es una columna (o un conjunto de columnas) en una tabla que se usa para identificar de manera única cada fila en esa tabla.

Características:

- Única: Los valores en una columna de clave primaria deben ser únicos para cada fila.
- No Nula: Los valores de una clave primaria no pueden ser nulos.
- Índice: Las claves primarias generalmente se indexan para mejorar el rendimiento de las consultas que buscan o filtran por la clave primaria.

## Clave Foránea (Foreign Key)

Una clave foránea es una columna (o un conjunto de columnas) en una tabla que crea una relación con la clave primaria de otra tabla.

Características:

- Relación: Establece una relación entre dos tablas, donde una tabla (la tabla hija) hace referencia a la clave primaria de otra tabla (la tabla padre).
- Integridad Referencial: Asegura que los valores en la columna de clave foránea existen en la columna de clave primaria de la otra tabla. Esto ayuda a mantener la integridad de los datos.

### `Primary Key (PK)`

```sql

CREATE TABLE "usuarios" (
	"id_usuarios"	INTEGER,
	"nombre"	TEXT,
	"apellido"	TEXT,
	"edad"	INTEGER,
	PRIMARY KEY("id_usuarios" AUTOINCREMENT)
);

 -->El AUTOINCREMENT es una propiedad de las clavez primarias

INSERT INTO usuarios (nombre,apellido,edad)
VALUES  ('Ramon','Juarez',21),
        ('Fernando','Solis',25)


```

| id_usuarios | nombre   | apellido | edad |
| ----------- | -------- | -------- | ---- |
| 1           | Ramon    | Juarez   | 21   |
| 2           | Fernando | Solis    | 25   |

`PK Campo que sirve para identificar registros`

### `Foreign Key (FK)`

```sql
 -->Se crea una tabla con nuestra llave primaria id_piso
CREATE TABLE "departamento" (
	"id_piso"	INTEGER,
	"Recepcionista"	TEXT,
     -->nuestro id_usuario hace referencia a nuestra tabla usuarios entonces es nuestro (FK)
	"id_usuario"	INTEGER,  --> Foreign Key
	"mantenimiento"	TEXT,
	PRIMARY KEY("id_piso" AUTOINCREMENT)
);


INSERT INTO departamento(Recepcionista,id_usuario,mantenimiento)

VALUES('MARIA FERNANDA',2,'SI');

SELECT * FROM departamento
```

`FK CAMPO QUE HACE REFERENCIA A UNA PK DE OTRA TABLA`

| id_piso | recepcionista  | _id_usuario_ | mantenimiento |
| ------- | -------------- | ------------ | ------------- |
| 1       | MARIA FERNANDA | 2            | SI            |

![alt text](image.png)
