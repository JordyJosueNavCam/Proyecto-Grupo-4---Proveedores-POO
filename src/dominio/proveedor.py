class Proveedor:
    def __init__(self, nombre=None, tipo=None, estado=None, ruc=None,
                 correo=None, telefono=None, direccion=None, fecha_registro=None):
        self._nombre = nombre
        self._tipo = tipo
        self._estado = estado
        self._ruc = ruc
        self._correo = correo
        self._telefono = telefono
        self._direccion = direccion
        self._fecha_registro = fecha_registro

    @property
    def nombre(self): return self._nombre
    @nombre.setter
    def nombre(self, valor): self._nombre = valor

    @property
    def tipo(self): return self._tipo
    @tipo.setter
    def tipo(self, valor): self._tipo = valor

    @property
    def estado(self): return self._estado
    @estado.setter
    def estado(self, valor): self._estado = valor

    @property
    def ruc(self): return self._ruc
    @ruc.setter
    def ruc(self, valor): self._ruc = valor

    @property
    def correo(self): return self._correo
    @correo.setter
    def correo(self, valor): self._correo = valor

    @property
    def telefono(self): return self._telefono
    @telefono.setter
    def telefono(self, valor): self._telefono = valor

    @property
    def direccion(self): return self._direccion
    @direccion.setter
    def direccion(self, valor): self._direccion = valor

    @property
    def fecha_registro(self): return self._fecha_registro
    @fecha_registro.setter
    def fecha_registro(self, valor): self._fecha_registro = valor

    def __str__(self):
        return (
            f"----------------------------\n"
            f"Información del Proveedor\n"
            f"----------------------------\n"
            f"Nombre: {self._nombre}\n"
            f"Tipo: {self._tipo}\n"
            f"Estado: {self._estado}\n"
            f"RUC: {self._ruc}\n"
            f"Correo: {self._correo}\n"
            f"Teléfono: {self._telefono}\n"
            f"Dirección: {self._direccion}\n"
            f"Fecha de registro: {self._fecha_registro or 'No especificada'}\n"
        )


if __name__ == '__main__':
    p = Proveedor('Favorita', 'Mayorista', 'Activo',
                  '1234567890111', 'aaa@aaa.com', '1234567890', 'Calle Ejemplo', '2023-01-01')
    print(p)
