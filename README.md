# HUELLITAS Veterinary Management System

El sistema de gestión veterinaria "HUELLITAS" es una plataforma integral diseñada para optimizar y facilitar la administración de una clínica veterinaria. Permite a los usuarios registrar y actualizar información de mascotas, gestionar citas, y acceder a historiales médicos completos y actualizados. Los veterinarios pueden consultar y editar servicios ofrecidos, mientras que los clientes pueden programar o cancelar citas y verificar la información de sus mascotas. Con una interfaz intuitiva y funcionalidades robustas, "HUELLITAS" asegura una gestión eficiente y una mejor atención a las mascotas.

En resumen es un sistema que facilita la atencion  mascotas tanto al veterinario como  los duenos.

## Tabla de Contenido

1. [Requerimientos](#requerimientos)
2. [Instalar Dependencias](#instalar-dependencias)
3. [Ejecutar el Proyecto](#ejecutar-el-proyecto)

### Requerimientos
- Trabajar sobre [Visual Studio Code](https://code.visualstudio.com/download)
- Instalar [Python](https://www.python.org/downloads/)
- Instalar [Node.js](https://nodejs.org/en/download/)
- Instalar [Django](https://www.djangoproject.com/download/)

### Instalar Dependencias
Ejecutar los siguientes comandos en la carpeta raíz

1. **Clone the repository**:
   ```console
   git clone https://github.com/your-username/huellitas-veterinary-system.git
### Backend
   1. **Navegar al directorio del backend**
      ```console
      cd veterinaria-1-no_borrar\proyecto_veterinaria\proyecto_veterinaria\mange.py
      ```
   2. **Install dependencies**:
      ```console
      pip install -r requirements.txt
      ```
   3.**Ejecutar el servidor backend:**
      ```console
        python manage.py migrate
        python manage.py runserver
      ```
### Frontend
   1. **Navegar al directorio del frontend**:
      ```console
      cd ../frontend
      ```
  2. **Install dependencies**:
      ```console
      npm install
      ```
### Ejecutar el Proyecto
   1. Configurar variables de entorno:
      Crear un archivo .env en el directorio backend y agregar las siguientes variables:
      ```console
      SECRET_KEY=your_secret_key
      DEBUG=True
      ALLOWED_HOSTS=localhost,127.0.0.1
      ```
   2. Ejecutar migraciones y el servidor backend:
      ```console
      python manage.py migrate
      python manage.py runserver
      ```
## Acceder a la Aplicación
  - Ir a http://localhost:5000 para el API del backend.
  - Abrir el archivo index.html en el navegador para usar la interfaz del sistema de gestión veterinaria HUELLITAS.
