# Proyecto Final: Python aplicado a sitios web con Django
Para el proyecto final del curso "Python" en Coderhouse se plantea el desarrollo de un sitio web con el framework Django. 

## We Domotic CRM
La propuesta es desarrollar un sitio web orientado a la gestión de proyectos mediante un panel de control y administracion de datos, basados en la lógica de sistemas CRM (Customer Relationship Management).

Las funcionalidades del sitio giran en torno gestionar listas de productos y clientes en una base datos. 
El objetivo final será simplificar el proceso de consulta y cotización de proyectos a los miembros del emprendimiento, que tendrán usuarios estándar.

El proceso de carga y/o edición estará limitada a usuarios con privilegios, que deben ser creados únicamente con superuser.

## Objetivos
El objetivo de la entrega y sus requisitos estan orientados al desarrollo de un sitio web estilo blog, incluyendo admin, perfiles, registro, publicaciones y formularios. 
Los requisitos base serán parte de los criterios de evaluación para aprobar el proyecto, en caso de querer cambiar de blog a otra temática.
### Requisitos base
- Video explicativo de 10 min máximo.
- Herencia de templates.
- `.gitignore` 
- `requirements.txt`
- Vistas:
    - Inicio/homepage
    - Acerca de mi/about
    - Listado de objetos del modelo principal. Cada objeto mostrará solo algunos de sus datos y mediante botones permite acceder a detalles.
        - Detalle de determinado objeto
        - Editar determinado objeto.
        - Crear objeto
        - Eliminar objeto
    - Autenticación:
        - Login
        - Logout
        - Sign up
        - Profile
        - Edit profile
        - Reset password
- Modelo principal (mínimo):
    - 2 Charfield
    - 1 Richtext
    - 1 Imagefield
    - 1 Datefield
- Características mínimas:
    - 2 vistas class-based.
    - Registrar todos los modelos en el Django admin.
    - App para el manejo de usuario/autenticación
    - Un mixin `LoginRequiredMixin` y un decorador `@login_required`
    - Datos de usuario que deben visualizarse en Profile
        - Nombre y Apellido
        - Email
        - Usuario
        - Avatar
        - Biografia/link/fecha de cumpleaños/etc
    - App de mensajería con todo lo necesario para que los usuarios puedan comunicarse entre sí por mensajes.

### Implementación
La herencia HTML sucede a partir del elemento padre `./templates/index.html`. El diseño esta basado en el siguiente template: `https://startbootstrap.github.io/startbootstrap-sb-admin-2/index.html`.

### Deployment
> [!NOTE] 
> Si bien el sitio continúa en etapa de desarrolo, se ha establecido la configuración `DEBUG = False` y `ALLOWED_HOSTS = [your.local.ip.address]` en `settings.py`. La finalidad es lograr el manejo automático de ciertas exceptions `Http404`, como así también habilitar el acceso al sitio desde otros dispositivos en la red local, como un teléfono móvil.

Lo anterior conlleva una desventaja: Django deja de servir los archivos estáticos. Es por esta razón que el servicio debe iniciarse estrictamente con el parámetro `--insecure`, y no debe omitirse la correcta declaración previa de la dirección IP (`127.0.0.1`, por ejemplo) en ALLOWED_HOSTS. De lo contrario se producirá **Bad Request (400)**

> [!IMPORTANT]
Es obligatorio iniciar el servicio como sigue, para evitar posibles errores:
```python manage.py runserver --insecure your.local.ip.address:port```

Para arrancar el servicio en su totalidad luego de clonar el repositorio, deben realizarse los siguientes pasos:
1. Crear entorno virtual: ```python -m venv /path/to/new/virtual/environment```
2. Arrancar el entorno virtual. Este comando depende del sistema, por ejemplo en bash: ```source venv_path/Scripts/Activate```
3. Instalar los paquetes necesarios: ```pip install -r requirements.txt```
4. Migracion de la base de datos: ```python manage.py migrate```
5. Crear superuser: ```python manage.py createsuperuser```
6. Configurar `ALLOWED_HOSTS` en `/config/settings.py`
7. Iniciar el servicio

![Logo](https://wedomotic.netlify.app/Images/logos/fondo.png)
<!-- 
### future updates*
- El título de cada clase de producto en el listado será un acceso a la ruta `/products/<product_class>/` para filtrar los productos por clase.
    - Cada producto mostrará una información mínima y tendrá un botón `**Detalles**` que permitirá acceder a todos los usuarios registrados a sus datos, en la ruta `/products/<product_class>/<product_id>` 
    - En esa vista, a usuarios con privilegios, les permitirá acceder a borrar y editar dicho objeto.
-->