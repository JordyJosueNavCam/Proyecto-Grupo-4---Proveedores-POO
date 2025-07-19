import re
from PySide6.QtGui import QIntValidator
from PySide6.QtWidgets import QMainWindow, QMessageBox
from datetime import datetime
from src.UI.vtnProveedor import Ui_Proveedores
from src.datos.ProveedorDao import ProveedorDao
from src.dominio.proveedor import Proveedor

class ProveedorServicio(QMainWindow):
    def __init__(self):
        super(ProveedorServicio, self).__init__()
        self.ui = Ui_Proveedores()
        self.ui.setupUi(self)

        self.ui.btnguardar.clicked.connect(self.guardar)
        self.ui.btnborrar.clicked.connect(self.borrar)
        self.ui.btnactualizar.clicked.connect(self.actualizar)
        self.ui.btnlimpiar.clicked.connect(self.limpiar)
        self.ui.btnbuscar.clicked.connect(self.buscar)

        self.ui.txtruc.setValidator(QIntValidator())
        self.ui.txttelefono.setValidator(QIntValidator())
        self.ui.txtbuscarruc.setValidator(QIntValidator())

    def validar_fecha(self, fecha):
        try:
            datetime.strptime(fecha, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def guardar(self):
        nombre = self.ui.txtnombre.text().strip()
        tipo = self.ui.cbtipo.currentText()
        estado = self.ui.cbestado.currentText()
        ruc = self.ui.txtruc.text().strip()
        correo = self.ui.txtcorreo.text().strip()
        telefono = self.ui.txttelefono.text().strip()
        direccion = self.ui.txtdireccion.text().strip()
        fecha_registro = self.ui.txtfecha.text().strip()

        if not nombre:
            QMessageBox.warning(self, 'Advertencia', 'Ingrese el nombre del proveedor.')
            return
        if tipo == 'Seleccionar':
            QMessageBox.warning(self, 'Advertencia', 'Seleccione un tipo de proveedor.')
            return
        if estado == 'Seleccionar':
            QMessageBox.warning(self, 'Advertencia', 'Seleccione un estado válido.')
            return
        if len(ruc) != 10:  # Verificar si el RUC tiene exactamente 10 caracteres
            QMessageBox.warning(self, 'Advertencia', 'El RUC debe tener 10 caracteres.')
            return
        if not correo or '@' not in correo or not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
            QMessageBox.warning(self, 'Advertencia', 'Ingrese un correo válido.')
            return
        if len(telefono) < 7:
            QMessageBox.warning(self, 'Advertencia', 'Ingrese un teléfono válido (mínimo 7 dígitos).')
            return
        if not direccion:
            QMessageBox.warning(self, 'Advertencia', 'Ingrese la dirección.')
            return

        if not fecha_registro or not self.validar_fecha(fecha_registro):
            QMessageBox.warning(self, 'Advertencia', 'Ingrese una fecha de registro válida (formato: YYYY-MM-DD).')
            return

        proveedor = Proveedor(
            nombre=nombre,
            tipo=tipo,
            estado=estado,
            ruc=ruc,
            correo=correo,
            telefono=telefono,
            direccion=direccion,
            fecha_registro=fecha_registro
        )

        print(f"Intentando guardar proveedor: {proveedor}")
        resultado = ProveedorDao.insertar_proveedor(proveedor)

        if resultado == -1:
            QMessageBox.critical(self, 'Error', 'No se pudo guardar el proveedor.')
        else:
            self.ui.statusbar.showMessage('Proveedor guardado exitosamente', 3000)
            self.limpiar()

    def limpiar(self):
        self.ui.txtnombre.setText("")
        self.ui.cbtipo.setCurrentText("Seleccionar")
        self.ui.cbestado.setCurrentText("Seleccionar")
        self.ui.txtruc.setText("")
        self.ui.txtbuscarruc.setText("")
        self.ui.txtcorreo.setText("")
        self.ui.txttelefono.setText("")
        self.ui.txtdireccion.setText("")
        self.ui.txtfecha.setText("")

    def buscar(self):
        ruc_buscar = self.ui.txtbuscarruc.text().strip()
        if len(ruc_buscar) != 10:  # Verificar si el RUC tiene exactamente 10 caracteres
            QMessageBox.warning(self, 'Advertencia', 'Ingrese el RUC a buscar (10 dígitos).')
            return

        proveedor = ProveedorDao.seleccionar_proveedor(ruc_buscar)
        if proveedor:
            self.ui.txtnombre.setText(proveedor.nombre)
            self.ui.cbtipo.setCurrentText(proveedor.tipo)
            self.ui.cbestado.setCurrentText(proveedor.estado)
            self.ui.txtruc.setText(proveedor.ruc)
            self.ui.txtcorreo.setText(proveedor.correo)
            self.ui.txttelefono.setText(proveedor.telefono)
            self.ui.txtdireccion.setText(proveedor.direccion)

            # Convertir la fecha de tipo datetime a string
            if isinstance(proveedor.fecha_registro, datetime):
                self.ui.txtfecha.setText(proveedor.fecha_registro.strftime('%Y-%m-%d'))
            else:
                self.ui.txtfecha.setText(proveedor.fecha_registro)  # Si ya es una cadena, no lo necesitas convertir
        else:
            QMessageBox.information(self, 'Información', 'RUC no encontrado.')

    def actualizar(self):
        if QMessageBox.question(self, 'Pregunta', '¿Está seguro de actualizar?') != QMessageBox.Yes:
            return

        nombre = self.ui.txtnombre.text().strip()
        tipo = self.ui.cbtipo.currentText()
        estado = self.ui.cbestado.currentText()
        ruc = self.ui.txtruc.text().strip()
        correo = self.ui.txtcorreo.text().strip()
        telefono = self.ui.txttelefono.text().strip()
        direccion = self.ui.txtdireccion.text().strip()
        fecha_registro = self.ui.txtfecha.text().strip()

        if not nombre:
            QMessageBox.warning(self, 'Advertencia', 'Ingrese el nombre del proveedor.')
            return
        if tipo == 'Seleccionar':
            QMessageBox.warning(self, 'Advertencia', 'Seleccione un tipo de proveedor.')
            return
        if estado == 'Seleccionar':
            QMessageBox.warning(self, 'Advertencia', 'Seleccione un estado válido.')
            return
        if len(ruc) != 10:  # Verificar si el RUC tiene exactamente 10 caracteres
            QMessageBox.warning(self, 'Advertencia', 'El RUC debe tener 10 caracteres.')
            return
        if not correo or '@' not in correo or not re.match(r'^[\w\.-]+@[\w\.-]+\.\w+$', correo):
            QMessageBox.warning(self, 'Advertencia', 'Ingrese un correo válido.')
            return
        if len(telefono) < 7:
            QMessageBox.warning(self, 'Advertencia', 'Ingrese un teléfono válido (mínimo 7 dígitos).')
            return
        if not direccion:
            QMessageBox.warning(self, 'Advertencia', 'Ingrese la dirección.')
            return

        # Validación de la fecha de registro
        if not fecha_registro or not self.validar_fecha(fecha_registro):
            QMessageBox.warning(self, 'Advertencia', 'Ingrese una fecha de registro válida (formato: YYYY-MM-DD).')
            return

        proveedor = Proveedor(
            nombre=nombre,
            tipo=tipo,
            estado=estado,
            ruc=ruc,
            correo=correo,
            telefono=telefono,
            direccion=direccion,
            fecha_registro=fecha_registro  # Asegúrate de que sea un string
        )

        print(f"Intentando actualizar proveedor: {proveedor}")
        resultado = ProveedorDao.actualizar_proveedor(proveedor)

        if resultado == -1:
            QMessageBox.critical(self, 'Error', 'No se pudo actualizar el proveedor.')
        else:
            self.ui.statusbar.showMessage('Proveedor actualizado exitosamente', 3000)
            self.limpiar()

    def borrar(self):
        if QMessageBox.question(self, 'Pregunta', '¿Está seguro de borrar el registro?') != QMessageBox.Yes:
            return

        ruc = self.ui.txtruc.text().strip()
        if not ruc or len(ruc) != 10:  # Verificar si el RUC tiene exactamente 10 caracteres
            QMessageBox.warning(self, 'Advertencia', 'Ingrese un RUC válido para borrar.')
            return

        resultado = ProveedorDao.eliminar_proveedor(ruc)

        if resultado == -1:
            QMessageBox.critical(self, 'Error', 'No se pudo borrar el registro del proveedor.')
        else:
            self.ui.statusbar.showMessage('Registro borrado exitosamente', 3000)
            self.limpiar()
