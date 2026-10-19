# 🎓 Sistema de Gestión de Alumnos

Aplicación web desarrollada con **Django** para administrar los alumnos y el
registro de asistencias del Instituto Superior del Milagro.

## ✨ Funcionalidades

- **CRUD completo de alumnos**: alta, listado, detalle, edición y baja.
- **Buscador** por nombre, apellido o email en una sola consulta (Q objects).
- **Estadísticas en tiempo real**: total de alumnos, activos e inactivos,
  calculadas con `aggregate()` directamente en la base de datos.
- **Control de asistencias**: registro de presente, ausente o tardanza con
  observaciones o justificativos, desde la ficha de cada alumno.
- **Validaciones de integridad**: legajo y email únicos, y una sola asistencia
  por alumno y por día (`unique_together`).
- **Autenticación**: alta, edición y baja protegidas con `@login_required`.
- **Mensajes de feedback** al usuario con el framework de mensajes de Django.

## 🧠 Conceptos y buenas prácticas aplicados

- Modelos con relaciones `ForeignKey` y `related_name`.
- Consultas con el ORM de Django: `filter`, `Q`, `Count`, `aggregate`.
- Patrón **POST-Redirect-GET** para evitar envíos duplicados de formularios.
- Eliminación solo por `POST` con pantalla de confirmación (protección contra
  borrados accidentales o maliciosos).
- Uso de `get_object_or_404` para un manejo de errores limpio.
- `ModelForm` para validación y guardado de datos.
- Código documentado con docstrings y comentarios.

## 🗂️ Modelos

| Modelo       | Campos principales                                          |
|--------------|-------------------------------------------------------------|
| `Alumno`     | nombre, apellido, email (único), legajo (único), activo, fecha_alta |
| `Asistencia` | alumno (FK), fecha, estado (Presente/Ausente/Tardanza), observaciones |

## 🛠️ Tecnologías

- Python 3
- Django
- HTML + templates de Django
- SQLite (por defecto)

## 🚀 Instalación y uso

```bash
# 1. Clonar el repositorio
git clone https://github.com/TU-USUARIO/NOMBRE-DEL-REPO.git
cd NOMBRE-DEL-REPO

# 2. Crear y activar un entorno virtual
python -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Aplicar migraciones
python manage.py migrate

# 5. Crear un superusuario
python manage.py createsuperuser

# 6. Iniciar el servidor
python manage.py runserver
```

Abrí `http://127.0.0.1:8000/alumnos/` en el navegador.

## 🔗 Rutas principales

| Ruta                          | Descripción                  | Requiere login |
|-------------------------------|------------------------------|:--------------:|
| `/alumnos/`                   | Listado, búsqueda y estadísticas | No         |
| `/alumnos/<legajo>/`          | Detalle y asistencias        | No             |
| `/alumnos/nuevo/`             | Alta de alumno               | Sí             |
| `/alumnos/<legajo>/editar/`   | Edición de alumno            | Sí             |
| `/alumnos/<legajo>/eliminar/` | Baja de alumno               | Sí             |

## 📌 Próximas mejoras

- Reportes de asistencia por alumno y por período.
- Exportación a Excel o PDF.
- Tests automatizados.
- Despliegue en producción.

## 👤 Autor

**Guillermo Sanchez Apaza** · [LinkedIn](https://www.linkedin.com/in/guille-apaza-9569b0355/) · [GitHub](https://github.com/Guillermovgs)
