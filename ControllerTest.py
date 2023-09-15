
# Todas las prueba sunitarias importan la biblioteca unittest
import unittest

from Usuario import Usuario
import ControladorUsuarios

class ControllerTest(unittest.TestCase):
    """
        Pruebas a la Clase Controlador de la aplicación
    """

    def testInsert(self):
        """ Verifica que funcione bien la creacion y la busqueda de un usuario """
        # Pedimos crear un usuario

        usuario_prueba = Usuario( "123456", "Usuario", "Prueba", "no@tiene.correo", "EN la calle", "99999", "05", "05001"  ) 

        ControladorUsuarios.Insertar( usuario_prueba )

        # Buscamos el usuario
        usuario_buscado = ControladorUsuarios.BuscarPorCedula( usuario_prueba.cedula )

        # Verificamos que los datos del usuario sean correcto
        self.assertEqual( usuario_prueba.cedula, usuario_buscado.cedula )
        self.assertEqual( usuario_prueba.nombre, usuario_buscado.nombre )
        self.assertEqual( usuario_prueba.apellido, usuario_buscado.apellido )
        self.assertEqual( usuario_prueba.direccion, usuario_buscado.direccion )
        self.assertEqual( usuario_prueba.correo, usuario_buscado.correo )
        self.assertEqual( usuario_prueba.telefono, usuario_buscado.telefono )
        self.assertEqual( usuario_prueba.codigo_departamento, usuario_buscado.codigo_departamento )
        self.assertEqual( usuario_prueba.codigo_municipio, usuario_buscado.codigo_municipio )




# Este fragmento de codigo permite ejecutar la prueb individualmente
# Va fijo en todas las pruebas
if __name__ == '__main__':
    # print( Payment.calcularCuota.__doc__)
    unittest.main()