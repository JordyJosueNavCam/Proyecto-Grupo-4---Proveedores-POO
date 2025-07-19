import sys
from PySide6.QtWidgets import QApplication
from src.servicio.proveedor import ProveedorServicio
if __name__ == "__main__":
    app = QApplication(sys.argv)
    vtnProveedor = ProveedorServicio()
    vtnProveedor.show()
    sys.exit(app.exec())
