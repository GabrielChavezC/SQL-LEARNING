import sqlite3  # Importar el módulo sqlite3 para interactuar con bases de datos SQLite
import pandas as pd  # Importar pandas para manipular y analizar datos en formato DataFrame

# Definir una función lambda que calcula el cubo de un número
square = lambda n: n * n * n

# Imprimir el cubo de 10 como prueba (esto imprimirá 1000)
print(square(10))

#======================================================================================================
                                 #1ra Forma para hacer la conexión BD
#======================================================================================================


# Conectarse a la base de datos SQLite
conn = sqlite3.connect('./database/sql/Nortwind.db')

# Crear una función personalizada en SQLite que usa la función 'square' definida en Python
# Esta función se puede utilizar en consultas SQL dentro de esta conexión
conn.create_function('square', 1, square)

# Crear un cursor para ejecutar consultas SQL
cursor = conn.cursor()

# Ejecutar una consulta SQL que selecciona todos los campos de la tabla 'Products'
# y calcula el cubo del precio con la función 'square', añadiendo el resultado como 'Precio_al_c3'
cursor.execute(
    '''
         SELECT *, square(Price) as Precio_al_c3 
         FROM Products           
    ''')

# Obtener todos los resultados de la consulta
results = cursor.fetchall()

# Obtener los nombres de las columnas de la consulta utilizando 'cursor.description'
column_names = [description[0] for description in cursor.description]

# Crear un DataFrame de pandas utilizando los resultados obtenidos y los nombres de las columnas
df_results = pd.DataFrame(results, columns=column_names)

# Cerrar el cursor y la conexión
cursor.close()
conn.close()

# Imprimir el DataFrame con los resultados de la consulta
print(df_results)


#======================================================================================================
                                 #2da Forma para hacer la conexión con WITH 
#======================================================================================================



# Usar 'with' para manejar la conexión a la base de datos, lo que asegura que se cierre correctamente
with sqlite3.connect('./database/sql/Nortwind.db') as conn:  
    # Crear la función personalizada 'square' en SQLite que usará la función lambda de Python
    conn.create_function('square', 1, square)
    
    # Crear un cursor para ejecutar consultas SQL
    cursor = conn.cursor()
    
    # Ejecutar una consulta SQL que selecciona todos los campos de la tabla 'Products'
    # y calcula el cubo del precio con la función 'square', añadiendo el resultado como 'Precio_al_c3'
    cursor.execute(
    '''
        SELECT *, square(Price) as Precio_al_c3 
        FROM Products
    ''')
    
    # Obtener todos los resultados de la consulta
    results1 = cursor.fetchall()
    
    # Obtener los nombres de las columnas, incluido el nuevo campo 'Precio_al_c2'
    column_names = [description[0] for description in cursor.description]
    
    # Crear un DataFrame de pandas usando los resultados de la consulta y las columnas obtenidas
    df_results1 = pd.DataFrame(results1, columns=column_names)

# Fuera del bloque 'with', imprimir el DataFrame resultante
print(df_results1)