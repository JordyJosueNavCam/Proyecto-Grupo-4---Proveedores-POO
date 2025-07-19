from src.datos.conexion import Conexion
from src.dominio.proveedor import Proveedor

class ProveedorDao:
    _ERROR = -1
    _INSERT = ("INSERT INTO Proveedores(nombre, tipo, ruc, correo, telefono, direccion, estado, fecha_registro) "
               "VALUES (?, ?, ?, ?, ?, ?, ?, ?)")
    _SELECT = ("SELECT nombre, tipo, estado, ruc, correo, telefono, direccion, fecha_registro "
               "FROM Proveedores WHERE ruc=?")
    _UPDATE = ("UPDATE Proveedores SET nombre=?, tipo=?, ruc=?, correo=?, telefono=?, direccion=?, estado=?, fecha_registro=? "
               "WHERE ruc=?")
    _DELETE = "DELETE FROM Proveedores WHERE ruc=?"

    @classmethod
    def insertar_proveedor(cls, proveedor):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (
                    proveedor.nombre,
                    proveedor.tipo,
                    proveedor.ruc,
                    proveedor.correo,
                    proveedor.telefono,
                    proveedor.direccion,
                    proveedor.estado,
                    proveedor.fecha_registro
                )
                registros = cursor.execute(cls._INSERT, datos)
                Conexion.obtenerConexion().commit()
                return registros.rowcount
        except Exception as e:
            print(f"Error al insertar proveedor: {e}")
            Conexion.obtenerConexion().rollback()
            return cls._ERROR

    @classmethod
    def seleccionar_proveedor(cls, ruc):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (ruc,)
                registro = cursor.execute(cls._SELECT, datos).fetchone()

                if not registro:
                    return None

                proveedor = Proveedor(
                    nombre=registro[0],
                    tipo=registro[1],
                    estado=registro[2],
                    ruc=registro[3],
                    correo=registro[4],
                    telefono=registro[5],
                    direccion=registro[6],
                    fecha_registro=registro[7]
                )

                return proveedor
        except Exception as e:
            print(f"Error al consultar proveedor: {e}")
            return None

    @classmethod
    def actualizar_proveedor(cls, proveedor):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (
                    proveedor.nombre,
                    proveedor.tipo,
                    proveedor.ruc,
                    proveedor.correo,
                    proveedor.telefono,
                    proveedor.direccion,
                    proveedor.estado,
                    proveedor.fecha_registro,
                    proveedor.ruc
                )
                registros = cursor.execute(cls._UPDATE, datos)
                Conexion.obtenerConexion().commit()
                return registros.rowcount
        except Exception as e:
            print(f"Error al actualizar proveedor: {e}")
            Conexion.obtenerConexion().rollback()
            return cls._ERROR

    @classmethod
    def eliminar_proveedor(cls, ruc):
        try:
            with Conexion.obtenerCursor() as cursor:
                datos = (ruc,)
                registros = cursor.execute(cls._DELETE, datos)
                Conexion.obtenerConexion().commit()
                return registros.rowcount
        except Exception as e:
            print(f"Error al eliminar proveedor: {e}")
            Conexion.obtenerConexion().rollback()
            return cls._ERROR

if __name__ == '__main__':
    proveedor_prueba = Proveedor('Prueba', 'Local', 'Activo', '9876543210001',
                                 'prueba@email.com', '0987654321', 'Calle X', '2025-07-19')
    resultado = ProveedorDao.insertar_proveedor(proveedor_prueba)
    print(f"Resultado insertar: {resultado}")
