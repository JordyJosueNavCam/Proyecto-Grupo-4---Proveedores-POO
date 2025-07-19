# Proyecto Final - Sistema de Gestión de Proveedores

**Carrera**: Gestión de la Información Gerencial  
**Materia**: Programación Orientada a Objetos

## Integrantes del Grupo 4:
- **Zury Luisana Gómez Mendoza**
- **Jordy Josué Navarrete Camba**
- **Rebeca Sarai Pinto Mejía**
- **Luis Enrique Ramírez Quinde**
- **José Joel Santillán Troya**

---

## **Descripción del Proyecto**

Este proyecto tiene como objetivo desarrollar un **Sistema de Gestión de Proveedores** diseñado para **optimizar y simplificar** los procesos de registro, actualización, consulta y eliminación de proveedores dentro de una empresa. La aplicación permite gestionar los datos esenciales de los proveedores, como:

- Nombre
- Tipo
- RUC
- Correo
- Teléfono
- Dirección
- Estado

La aplicación estará **basada en Programación Orientada a Objetos (POO)**, utilizando **Python**, con la biblioteca **PySide6** para la interfaz gráfica y **pyodbc** para la conexión con la base de datos **SQL Server**.

---

## **Objetivos del Proyecto**

1. **Optimización** de los procesos administrativos de los proveedores.
2. **Mejora de la calidad de los datos** mediante validaciones en tiempo real.
3. **Interfaz amigable y eficiente** para los usuarios no técnicos.
4. **Gestión centralizada** de proveedores en una base de datos segura y confiable.

---

## **Funcionalidades del Sistema**

### 1. **Registro de Proveedores**
   Permite ingresar nuevos proveedores al sistema con validaciones de datos (RUC, correo y teléfono), asegurando la calidad y consistencia de la información.

### 2. **Consulta de Proveedores**
   Los usuarios pueden buscar proveedores mediante su RUC para consultar los datos registrados de manera rápida y eficiente.

### 3. **Actualización de Información**
   Los usuarios pueden modificar la información de proveedores ya existentes (nombre, correo, teléfono, etc.).

### 4. **Eliminación de Proveedores**
   Permite eliminar un proveedor por su RUC, borrando sus datos del sistema de forma definitiva.

---

## **Flujo de Funcionamiento del Sistema**

### **1. Conexión a la Base de Datos**

El sistema establece una conexión con la base de datos **SQL Server** utilizando la librería **pyodbc**. La clase `Conexion` se encarga de gestionar esta conexión y proporciona un cursor para ejecutar las consultas SQL necesarias para la manipulación de los datos.

### **2. Interfaz Gráfica de Usuario (UI)**

La **interfaz gráfica** está desarrollada con **PySide6**, permitiendo una interacción intuitiva. En la UI, los usuarios podrán ingresar y visualizar los datos de los proveedores de forma fácil. Los campos disponibles incluyen:

- Nombre
- RUC
- Correo
- Teléfono
- Dirección
- Tipo de Proveedor
- Estado del Proveedor
- Fecha de Registro

### **3. Operaciones CRUD**

El sistema permite realizar las operaciones estándar de gestión de datos:

- **Crear**: Permite agregar nuevos proveedores a la base de datos.
- **Leer**: Consulta y visualización de la información de un proveedor mediante su RUC.
- **Actualizar**: Modificación de los datos de un proveedor ya registrado.
- **Eliminar**: Eliminación de un proveedor a través de su RUC.

### **4. Validaciones**

El sistema implementa validaciones para asegurar la correcta entrada de datos:

- **RUC**: El RUC debe tener **exactamente 10 caracteres**.
- **Teléfono**: El teléfono debe tener al menos **7 caracteres**.
- **Correo**: El correo debe seguir un formato estándar (ejemplo: `correo@dominio.com`).
- **Fecha de Registro de Proveedor**:
   - La **fecha de registro** se asigna **automáticamente** utilizando la fecha y hora actuales al momento de ingresar un proveedor, garantizando que siempre se mantenga un registro preciso de cuándo fue añadido un nuevo proveedor.
   - **Formato de la Fecha**: La fecha se almacenará en el formato `YYYY-MM-DD`, asegurando la uniformidad en la base de datos.
   - **Asignación automática**: La fecha es generada automáticamente por el sistema, sin necesidad de intervención del usuario.

---

## **Conclusión**

Este sistema de gestión de proveedores no solo automatiza y optimiza los procesos internos de la empresa, sino que también garantiza la integridad y consistencia de los datos a través de estrictas validaciones. La solución propuesta, basada en **Programación Orientada a Objetos (POO)**, ofrece una interfaz gráfica amigable para el usuario y una conexión eficiente con la base de datos. Este proyecto busca mejorar la eficiencia en la gestión de proveedores, ahorrando tiempo y recursos, y facilitando el acceso a la información en tiempo real.

---



