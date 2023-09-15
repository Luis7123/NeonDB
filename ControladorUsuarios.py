"""
    Controla las operaciones de almacenamiento de la clase Usuario
"""
from Usuario import Usuario
import sys
import psycopg2


def ObtenerCursor():
    '''
    Crea la conexion a la base de datos y retorna un cursor para ejecutar instrucciones.

    '''
    DATABASE="neondb"
    USER="Luis7123"
    PASSWORD="XEV9Cv0nsbjp"
    HOST="ep-sparkling-sky-88751575.us-east-2.aws.neon.tech"
    connection= psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=5432)
    return connection.cursor()
    
def Insertar( usuario : Usuario ):
    """ Guarda un Usuario en la base de datos """

    # Reemplace los datos de conexion con los datos tomados de su servidor
    connection = psycopg2.connect(database="neondb", user="Luis7123", password="XEV9Cv0nsbjp", host="ep-sparkling-sky-88751575.us-east-2.aws.neon.tech", port=5432)
        
    try:

        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = connection.cursor()
        cursor.execute(f"""
        insert into usuarios (
            cedula,   nombre,  apellido,  telefono,  correo, direccion, codigo_municipio, codigo_departamento
        )
        values 
        (
            '{usuario.cedula}',  '{usuario.nombre}', '{usuario.apellido}', '{usuario.telefono}', '{usuario.correo}', '{usuario.direccion}', '{usuario.codigo_municipio}', '{usuario.codigo_departamento}'
        );
                       """)

        # Las instrucciones DDL y DML no retornan resultados, por eso no necesitan fetchall()
        # pero si necesitan commit() para hacer los cambios persistentes

        connection.commit()
    except  :
        connection.rollback() 
        raise Exception("No fue posible insertar el usuario : " + usuario.cedula )
    
def BuscarPorCedula( cedula :str ):    
    """ Busca un usuario por el numero de Cedula """
    connection = psycopg2.connect(database="neondb", user="ProfeBill", password="O4oU5naNIuRe", host="ep-round-mountain-97326230.us-east-2.aws.neon.tech", port=5432)
    # Todas las instrucciones se ejecutan a tavés de un cursor
    cursor = connection.cursor()
    cursor.execute(f"SELECT cedula,   nombre,  apellido,  telefono,  correo, direccion, codigo_municipio, codigo_departamento from usuarios where cedula = '{cedula}' ")
    fila = cursor.fetchone()

    resultado = Usuario( fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7])
    return resultado