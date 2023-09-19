"""
    Pertenece a la capa de Acceso a Datos

    Controla las operaciones de almacenamiento de la clase Usuario
"""
from Usuario import Usuario

import sys
import psycopg2
import SecretConfig

def ObtenerCursor( ) :
    """
    Crea la conexion a la base de datos y retorna un cursor para ejecutar instrucciones
    """
    DATABASE = SecretConfig.DATABASE
    USER = SecretConfig.USER
    PASSWORD = SecretConfig.PASSWORD
    HOST = SecretConfig.HOST
    PORT = SecretConfig.PORT
    connection = psycopg2.connect(database=DATABASE, user=USER, password=PASSWORD, host=HOST, port=PORT)
    return connection.cursor()

    

def Insertar( usuario : Usuario ):
    """ Guarda un Usuario en la base de datos """

    try:

        # Todas las instrucciones se ejecutan a tavés de un cursor
        cursor = ObtenerCursor()
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
        cursor.connection.commit()
    except  :
        cursor.connection.rollback() 
        raise Exception("No fue posible insertar el usuario : " + usuario.cedula )
    
def BuscarPorCedula( cedula :str ):    
    """ Busca un usuario por el numero de Cedula """

    # Todas las instrucciones se ejecutan a tavés de un cursor
    cursor = ObtenerCursor()
    cursor.execute(f"SELECT cedula,nombre,apellido,correo,direccion,telefono,codigo_departamento,codigo_municipio from usuarios where cedula = '{cedula}' ")
    fila = cursor.fetchone()

    resultado = Usuario( fila[0], fila[1], fila[2], fila[3], fila[4], fila[5], fila[6], fila[7])
    return resultado

def Actualizar( usuario : Usuario ):
    """
    Actualiza los datos de un usuario en la base de datos

    El atributo cedula nunca se debe cambiar, porque es la clave primaria
    """
    cursor = ObtenerCursor()
    cursor.execute(f"""
        update usuarios
        set 
            nombre='{usuario.nombre}',
            apellido='{usuario.apellido}',
            telefono='{usuario.telefono}',
            direccion='{usuario.direccion}',
            correo='{usuario.correo}',
            codigo_departamento='{usuario.codigo_departamento}',
            codigo_municipio='{usuario.codigo_municipio}'
        where cedula='{usuario.cedula}'
    """)
    # Las instrucciones DDL y DML no retornan resultados, por eso no necesitan fetchall()
    # pero si necesitan commit() para hacer los cambios persistentes
    cursor.connection.commit()

