# 📚 Gestor de Colecciones Personalizadas

Una aplicación web moderna para gestionar colecciones (libros, películas, juegos, etc.) construida con **FastAPI**, **PostgreSQL** y **Tailwind CSS**.

![Home](https://github.com/MarioPortacio/gestor-colecciones/blob/73bbcd52850d27c156fd80d6b076606c59c902a6/img/p1.jpg)

![Img 2](https://github.com/MarioPortacio/gestor-colecciones/blob/73bbcd52850d27c156fd80d6b076606c59c902a6/img/p2.jpg)

![Img 3](https://github.com/MarioPortacio/gestor-colecciones/blob/73bbcd52850d27c156fd80d6b076606c59c902a6/img/p3.jpg)



## ✨ Características
- **Backend robusto:** FastAPI con validación de datos y ORM (SQLAlchemy).
- **Base de datos:** PostgreSQL para persistencia de datos.
- **Frontend moderno:** Diseño responsive con Tailwind CSS v4.
- **Validación visual:** Sistema de puntuación con estrellas y categorías dinámicas.
- **Optimización:** CSS compilado y minificado para producción.
- **UX/UI:** Sistema de estrellas, categorías dinámicas y validaciones estéticas.

## 🛠️ Tecnologías utilizadas

### Backend 📝
- **Python 3.12+**: Lenguaje base del proyecto.
- **FastAPI**: Framework web asíncrono de alto rendimiento.
- **SQLAlchemy**: ORM para la gestión de la base de datos.
- **Pydantic**: Validación de esquemas y tipos de datos.
- **Uvicorn**: Servidor ASGI para la ejecución de la app.
- **Psycopg2**: Adaptador de base de datos para PostgreSQL.

### Frontend 🎨
- **Tailwind CSS v4**: Framework de diseño compilado mediante CLI para máximo rendimiento.
- **JavaScript (Vanilla)**: Lógica interactiva del lado del cliente.
- **HTML5 & CSS3**: Estructura y estilos base.

### DevOps & Tools 💻
- **Git & GitHub**: Control de versiones.
- **Render**: Plataforma de despliegue (Cloud Hosting).
- **PostgreSQL**: Motor de base de datos relacional.

## 🔧 Configuración Local

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/MarioPortacio/gestor-colecciones.git
   cd gestor_colecciones
   python -m venv venv
   ./venv/Scripts/activate
   pip install -r requirements.txt

2. **Entorno virtual:**
    ```bash
    python -m venv venv
    ./venv/Scripts/activate
    pip install -r requirements.txt

3. **Variables de Entorno (.env): Crea un archivo .env con tus credenciales y pega:**
    ```bash
    DB_USER=postgres(o tu_usuariodb)
    DB_PASSWORD=tu_contraseña
    DB_HOST=localhost
    DB_PORT=5432
    DB_NAME=colecciones_db

4. **Ejecutar la App:**
    ```bash
    uvicorn main:app --reload


## 📈 Posibles mejoras futuras

- **Autenticación de Usuarios:** Implementar login y registro con JWT para que cada usuario tenga su propia colección privada.

- **Subida de Imágenes:** Permitir que los usuarios suban fotos de sus colecciones (portadas de libros, carátulas de juegos) usando servicios como Cloudinary o AWS S3.

- **Búsqueda Avanzada y Filtros:** Añadir un buscador en tiempo real y filtros por fecha de adquisición.

- **Modo Oscuro (Dark Mode):** Implementar un selector de temas usando las capacidades nativas de Tailwind CSS.

- **Exportación de Datos:** Botón para exportar la colección actual a formato CSV o PDF.

- **Estadísticas Dinámicas:** Un panel (dashboard) que muestre gráficos estadísticos.
